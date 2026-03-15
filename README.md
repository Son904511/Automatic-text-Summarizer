# 🧠 NLP Text Summarizer (Extractive + Abstractive)

An NLP-based web application that summarizes long text using **Extractive (TF-IDF)** and **Abstractive (DistilBART Transformer)** techniques.  
The application also provides **side-by-side comparison** and **compression ratio metrics** to evaluate summarization performance.

---

# 🚀 Features

- ✂️ **Extractive Summarization**
  - Uses TF-IDF and word frequency scoring
  - Selects the most relevant sentences from the original text

- 🤖 **Abstractive Summarization**
  - Uses the DistilBART Transformer model
  - Generates a human-like summary

- 📊 **Side-by-Side Comparison**
  - Compare extractive and abstractive summaries

- 📉 **Compression Ratio Metrics**
  - Displays how much the original text was reduced

- 🌐 **Simple Web Interface**
  - Lightweight frontend built using HTML, CSS, and JavaScript

---

# 🏗️ Tech Stack

| Layer | Technology |
|------|------------|
| Language | Python 3.10+ |
| Backend | Flask (REST API) |
| Frontend | HTML, CSS, JavaScript |
| NLP Libraries | NLTK, Scikit-learn |
| Deep Learning | HuggingFace Transformers |
| Model | `sshleifer/distilbart-cnn-12-6` |
| Framework | PyTorch |

---

# 📂 Project Structure

```
text-summarizer/
│
├── backend/
│   ├── app.py               # Flask REST API
│   ├── extractive.py        # TF-IDF summarizer
│   ├── abstractive.py       # DistilBART transformer summarizer
│   └── requirements.txt     # Python dependencies
│
└── frontend/
    └── index.html           # Web interface
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
```

### 2️⃣ Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3️⃣ Download required NLTK data

Run this once in Python:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
```

### 4️⃣ Start the Flask server

```bash
python app.py
```

### 5️⃣ Open the frontend

Open the following file in your browser:

```
frontend/index.html
```

---

# 🔗 API Endpoints

| Method | Endpoint | Description |
|------|-----------|-------------|
| GET | `/health` | Check server status |
| POST | `/summarize/extractive` | TF-IDF summarization |
| POST | `/summarize/abstractive` | DistilBART summarization |
| POST | `/summarize/compare` | Compare both methods |

---

# 📡 Example API Request

```bash
curl -X POST http://localhost:5000/summarize/extractive \
-H "Content-Type: application/json" \
-d '{"text": "Your long text here...", "num_sentences": 3}'
```

---

# 📥 Example Response

```json
{
  "summary": "Generated summary text.",
  "method": "Extractive (TFIDF)",
  "original_word_count": 320,
  "summary_word_count": 64,
  "compression_ratio": "80.0%"
}
```

---

# ⚙️ How It Works

### Extractive Summarization (TF-IDF)

1. Clean and tokenize the text  
2. Compute TF-IDF scores for each word  
3. Score sentences using the sum of their word scores  
4. Select the top N highest scoring sentences  
5. Return them in their original order  

---

### Abstractive Summarization (DistilBART)

1. Convert text into subword tokens  
2. Pass tokens through the transformer encoder  
3. Generate contextual embeddings  
4. Produce a summary token-by-token using beam search decoding  

---

### Compression Ratio

```
Compression Ratio = (1 − Summary Words / Original Words) × 100%
```

This metric indicates how much the original text has been reduced.

---

# 📦 Dependencies

```
flask==3.0.0
flask-cors==4.0.0
nltk==3.8.1
scikit-learn==1.3.2
numpy==1.26.2
transformers==4.36.0
torch==2.1.1
sentencepiece==0.1.99
```

---

# ⚠️ Notes

- The abstractive model downloads **~500MB on first run** and then caches locally.
- Texts longer than **700 words are automatically truncated** before abstractive processing.
- Extractive summarization works **fully offline**.
- Minimum input length:
  - **30 words** for Extractive
  - **50 words** for Abstractive

---

# 🔮 Future Improvements

- ROUGE score evaluation  
- PDF and document upload support  
- Multilingual summarization using mBART  
- BERT-based sentence scoring  
- Keyword extraction feature  

---

# 👨‍💻 Author

**Tushar Aggarwal**

Computer Science Student | AI & NLP Enthusiast
