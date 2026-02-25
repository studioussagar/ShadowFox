# spellcheck.py

def spelling_check(sentence, vocab, spell):
    words = sentence.split()
    corrected_words = []

    for w in words:
        if w in vocab:
            corrected_words.append(w)
        else:
            suggestion = spell.correction(w)
            if suggestion and suggestion in vocab:
                corrected_words.append(suggestion)
            else:
                corrected_words.append(w)

    return " ".join(corrected_words)