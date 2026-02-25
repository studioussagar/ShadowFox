import numpy as np
from collections import Counter
from .temperature import sample_with_temperature


# -------------------------------------------------------
# Trigram Predictor
# -------------------------------------------------------

def predict_trigram(sentence, trigram_model, k=3):
    words = sentence.split()

    if len(words) < 2:
        return []

    key = (words[-2], words[-1])

    if key not in trigram_model:
        return []

    freq = Counter(trigram_model[key])
    predictions = [w for w, _ in freq.most_common(k)]

    return predictions


# -------------------------------------------------------
# LSTM 2-word context Predictor
# -------------------------------------------------------

def predict_lstm2(sentence, model_2, word_index, index_word, k=3):
    words = sentence.split()

    if len(words) < 2:
        return []

    w1, w2 = words[-2], words[-1]

    if w1 not in word_index or w2 not in word_index:
        return []

    sequence = np.array([[word_index[w1], word_index[w2]]])
    preds = model_2.predict(sequence, verbose=0)[0]

    top_indices = sample_with_temperature(preds, temperature=0.7, k=k)

    results = []
    for idx in top_indices:
        word = index_word.get(idx)
        if word and word not in results:
            results.append(word)

    return results


# -------------------------------------------------------
# LSTM 3-word context Predictor
# -------------------------------------------------------

def predict_lstm3(sentence, model_3, word_index, index_word, k=3):
    words = sentence.split()

    if len(words) < 3:
        return []

    w1, w2, w3 = words[-3], words[-2], words[-1]

    if any(w not in word_index for w in [w1, w2, w3]):
        return []

    sequence = np.array([[word_index[w1], word_index[w2], word_index[w3]]])
    preds = model_3.predict(sequence, verbose=0)[0]

    top_indices = sample_with_temperature(preds, temperature=0.7, k=k)

    results = []
    for idx in top_indices:
        word = index_word.get(idx)
        if word and word not in results:
            results.append(word)

    return results