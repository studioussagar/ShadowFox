def spelling_check(sentence, vocab, spell):
    words = sentence.split()
    corrected_words = []

    for w in words:
        if w in vocab:
            corrected_words.append(w)
        else:
            correction = spell.correction(w)
            corrected_words.append(correction if correction else w)

    return " ".join(corrected_words)
