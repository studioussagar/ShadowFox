# core/ultimate.py

from .preprocess import preprocess
from .spellcheck import spelling_check
from .predictors import predict_trigram, predict_lstm2, predict_lstm3
from .merger import merge_predictions
from .splitter import OptimizedVocabSpellChecker
from .loader import (
    model_2, model_3,
    word_index, index_word,
    vocab, trigram_model,
    spell
)

splitter = OptimizedVocabSpellChecker(vocab)


# -------------------------------------------------------
# Context scoring using trigram
# -------------------------------------------------------

def context_score(sentence):
    words = sentence.split()
    score = 0

    for i in range(len(words) - 1):
        key = (words[i], words[i+1])
        if key in trigram_model:
            score += 1

    return score


# -------------------------------------------------------
# Intelligent split + correction
# -------------------------------------------------------

def intelligent_split_and_correct(sentence):
    words = sentence.split()
    final_words = []

    for w in words:

        if w in vocab:
            final_words.append(w)
            continue

        candidates = splitter.split_and_correct(w)

        # If splitter returns single correction list
        if isinstance(candidates[0], str):
            candidates = [candidates]

        best_candidate = [w]
        best_score = -1

        for cand_words in candidates:
            test_sentence = " ".join(final_words + cand_words)
            score = context_score(test_sentence)

            if score > best_score:
                best_score = score
                best_candidate = cand_words

        final_words.extend(best_candidate)

    return " ".join(final_words)


# -------------------------------------------------------
# FINAL HYBRID PREDICTOR
# -------------------------------------------------------

def ultimate_predictor(sentence, k=3):

    original_sentence = sentence

    # 1️⃣ Preprocess
    sentence = preprocess(sentence)

    # 2️⃣ Intelligent split
    sentence = intelligent_split_and_correct(sentence)

    # 3️⃣ Spell correction pass
    sentence = spelling_check(sentence, vocab, spell)

    corrected_sentence = sentence

    # 4️⃣ Predictions
    l3_preds  = predict_lstm3(sentence, model_3, word_index, index_word, k=5)
    tri_preds = predict_trigram(sentence, trigram_model, k=5)
    l2_preds  = predict_lstm2(sentence, model_2, word_index, index_word, k=5)

    # ------------------------
    # Merge Logic
    # ------------------------

    if not l3_preds and not tri_preds:
        final_preds = l2_preds[:k]

    elif not l3_preds:
        final_preds = []
        seen = set()

        for w in tri_preds + l2_preds:
            if len(final_preds) >= k:
                break
            if w not in seen:
                final_preds.append(w)
                seen.add(w)

    else:
        valid_context = set(l3_preds) | set(tri_preds)
        filtered_l2 = [w for w in l2_preds if w in valid_context]

        final_preds = merge_predictions(tri_preds, filtered_l2, l3_preds, k=k)

        seen = set(final_preds)
        for w in (l3_preds + tri_preds):
            if len(final_preds) >= k:
                break
            if w not in seen:
                final_preds.append(w)
                seen.add(w)

    return {
        "original": original_sentence,
        "corrected": corrected_sentence,
        "suggestions": final_preds
    }