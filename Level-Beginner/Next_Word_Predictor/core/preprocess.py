import string

def preprocess(sentence):
    for ch in string.punctuation:
        sentence = sentence.replace(ch, "")
    sentence = sentence.replace("\t", "")
    sentence = sentence.lower()
    return sentence
