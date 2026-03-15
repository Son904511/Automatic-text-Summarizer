📌 Project Overview
The Automatic Text Summarizer is an NLP-based application that takes any long piece of text as input and generates a concise, meaningful summary. It implements two summarization techniques — Extractive (TF-IDF) and Abstractive (DistilBART Transformer) — and provides a side-by-side comparison of both methods through an interactive web interface.

🛠️ Tech Stack
LayerTechnologyLanguagePython 3.10+BackendFlask (REST API)FrontendHTML, CSS, JavaScriptNLP LibraryNLTK, Scikit-learnDeep LearningHuggingFace Transformers (DistilBART)Modelsshleifer/distilbart-cnn-12-6

📁 Project Structure
text-summarizer/
├── backend/
│   ├── app.py               # Flask REST API (3 endpoints)
│   ├── extractive.py        # TF-IDF & word frequency summarizer
│   ├── abstractive.py       # DistilBART transformer summarizer
│   └── requirements.txt     # Python dependencies
└── frontend/
    └── index.html           # Web UI (3 modes)

⚙️ Installation & Setup
Step 1 — Clone the Repository
bashgit clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
Step 2 — Install Dependencies
bashcd backend
pip install -r requirements.txt
Step 3 — Download NLTK Data
Run this once in Python before starting the server:
pythonimport nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
Step 4 — Start the Flask Server
bashpython app.py
The server will start at http://localhost:5000
Step 5 — Open the Frontend
Open frontend/index.html in any browser. No additional setup needed.

🚀 Usage

Open the web interface in your browser
Select a summarization mode from the tabs
Paste your text into the input area (minimum 30 words)
Adjust the slider for number of sentences or output length
Click → Summarize
View the summary along with word count and compression ratio


🔁 API Endpoints
MethodEndpointDescriptionGET/healthCheck if the server is runningPOST/summarize/extractiveTF-IDF or word frequency summarizationPOST/summarize/abstractiveDistilBART transformer summarizationPOST/summarize/compareRun both methods and return side-by-side
Example Request (Extractive)
bashcurl -X POST http://localhost:5000/summarize/extractive \
  -H "Content-Type: application/json" \
  -d '{"text": "Your long text here...", "num_sentences": 3}'
Example Response
json{
  "summary": "Generated summary text here.",
  "method": "Extractive (TFIDF)",
  "original_word_count": 320,
  "summary_word_count": 64,
  "compression_ratio": "80.0%"
}
```

---

## 🧠 How It Works

### Extractive Summarization (TF-IDF)
1. Text is cleaned, tokenized, and stopwords are removed
2. TF-IDF scores are computed for every word across all sentences
3. Each sentence receives a score = sum of its word TF-IDF values
4. Top-N highest scoring sentences are selected and returned in original order

### Abstractive Summarization (DistilBART)
1. Input text is tokenized into subword tokens
2. The transformer encoder creates contextual embeddings for all tokens
3. The decoder generates a new summary token by token using beam search
4. Output tokens are decoded back into readable text

---

## 🖥️ Interface Modes

| Mode | Description |
|---|---|
| **Extractive (TF-IDF)** | Picks the most important sentences from the original text |
| **Abstractive (BART)** | Generates entirely new sentences using a transformer model |
| **Compare Both** | Runs both methods and shows results side by side |

---

## 📊 Output Metrics

After every summarization, the system displays:

- **Original Word Count** — total words in the input text
- **Summary Word Count** — total words in the generated summary
- **Compression Ratio** — percentage of text reduced, calculated as:
```
Compression Ratio = (1 - Summary Words / Original Words) × 100%
```

---

## 📦 Dependencies
```
flask==3.0.0
flask-cors==4.0.0
nltk==3.8.1
scikit-learn==1.3.2
numpy==1.26.2
transformers==4.36.0
torch==2.1.1
sentencepiece==0.1.99
Install all at once:
bashpip install -r backend/requirements.txt

⚠️ Notes

The abstractive model downloads ~500MB on first use. Subsequent runs use the cached model.
Texts longer than 700 words are automatically truncated before abstractive processing due to transformer token limits.
The extractive method works offline with no model download required.
Minimum input length is 30 words for extractive and 50 words for abstractive mode.


🔮 Future Improvements

ROUGE score evaluation for summary quality measurement
PDF and document file upload support
Multilingual summarization using multilingual transformer models
BERT-based sentence scoring for improved extractive results
Keyword extraction alongside summarization
Custom fine-tuned models for domain-specific text (medical, legal, academic)
