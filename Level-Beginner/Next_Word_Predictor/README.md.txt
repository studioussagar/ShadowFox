# AI-Powered Spell Checker & Next Word Predictor

An intelligent text prediction system combining:

- ✅ 3-word LSTM Language Model (Primary)
- ✅ 2-word LSTM Language Model (Secondary)
- ✅ Trigram Statistical Model (Fallback)
- ✅ Advanced Word Split + Spell Correction Engine

This system performs:

- 🔤 Automatic spell correction
- 🔎 Detection of accidentally joined words (e.g., `loveinthe` → `love in the`)
- 🧠 Context-aware next word prediction
- ⚡ Real-time prediction API using Flask

---

## 🚀 Project Architecture

Pipeline:

1. Preprocessing (lowercase, punctuation removal)
2. Word Split Correction (DP-based segmentation + spell correction)
3. Spell Checking
4. Multi-model Prediction:
   - 3-word LSTM (highest priority)
   - Trigram Model
   - 2-word LSTM (controlled influence)
5. Weighted Prediction Merge

---

## 🧠 Models Used

| Model | Context Size | Role |
|--------|--------------|------|
| LSTM 3-word | 3 previous words | Primary predictor |
| LSTM 2-word | 2 previous words | Secondary |
| Trigram | 2-word statistical | Baseline fallback |

---

## 📂 Project Structure
SpellChecker/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│ ├── lstm_3word_800k_e75_final.keras
│ ├── nextword_lstm_200k.keras
│ ├── tokenizer.pkl
│ ├── trigram.pkl
│ ├── vocab.pkl
│
├── templates/
│ └── index.html
│
└── static/
├── style.css
└── script.js


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your_repo_url>
cd SpellChecker

2️⃣ Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate     # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py


Then open:

http://127.0.0.1:5000

📊 Model Details

Training dataset: Movie dialogue corpus (~4.5M tokens)

3-word LSTM trained on ~800k tokens

75+ epochs training

Custom tokenizer and vocabulary

Dynamic temperature sampling for better diversity

📌 Notes for Internship Review

The 2-word LSTM training logic was removed from the final notebook for clarity.

Only the 3-word LSTM training implementation is retained in the training version.

The deployed application uses pre-trained models stored in /models.

Training code is intentionally separated from deployment code to avoid accidental retraining and to follow production best practices.

🧪 Example Predictions

Input:

What are you giong


Output:

doing
going
talking


Input:

I loveintheyou


Corrected:

i love in the you

🛠 Technologies Used

Python

TensorFlow / Keras

Flask

NumPy

pyspellchecker

HTML / CSS / JavaScript

🔮 Future Improvements

Transformer-based prediction model

Beam search decoding

Real-time incremental learning

REST API deployment