import pickle
from tensorflow.keras.models import load_model
from spellchecker import SpellChecker

# Load models
model_3 = load_model("models/lstm_3word_800k_e75_final.keras")
model_2 = load_model("models/nextword_lstm_200k.keras")

# Load tokenizer
with open("models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

word_index = tokenizer.word_index
index_word = {v: k for k, v in word_index.items()}
vocab = set(word_index.keys())

# Load trigram
with open("models/trigram.pkl", "rb") as f:
    trigram_model = pickle.load(f)

# Global spell
spell = SpellChecker()
