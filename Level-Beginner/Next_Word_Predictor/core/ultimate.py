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

def ultimate_predictor(sentence, k=3):

    sentence = preprocess(sentence)
    sentence = splitter.split(sentence)
    sentence = spelling_check(sentence, vocab, spell)

    l3_preds  = predict_lstm3(sentence, model_3, word_index, index_word, k=5)
    tri_preds = predict_trigram(sentence, trigram_model, k=5)
    l2_preds  = predict_lstm2(sentence, model_2, word_index, index_word, k=5)

    if not l3_preds and not tri_preds:
        return l2_preds[:k]

    if not l3_preds:
        primary = tri_preds
        secondary = l2_preds

        seen = set(primary[:k])
        result = list(primary[:k])

        for w in secondary:
            if len(result) >= k:
                break
            if w not in seen:
                result.append(w)
                seen.add(w)

        return result

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

    return final_preds
