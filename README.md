An NLP-based web application that summarizes long text using Extractive (TF-IDF) and Abstractive (DistilBART Transformer) techniques, with a side-by-side comparison mode and compression ratio metrics.

Tech Stack
LayerTechnologyLanguagePython 3.10+BackendFlask (REST API)FrontendHTML, CSS, JavaScriptNLP LibraryNLTK, Scikit-learnDeep LearningHuggingFace TransformersModelsshleifer/distilbart-cnn-12-6

Project Structure
text-summarizer/
├── backend/
│   ├── app.py               # Flask REST API
│   ├── extractive.py        # TF-IDF & word frequency summarizer
│   ├── abstractive.py       # DistilBART transformer summarizer
│   └── requirements.txt     # Python dependencies
└── frontend/
    └── index.html           # Web UI

Installation
bash# 1. Clone the repository
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer

# 2. Install dependencies
cd backend
pip install -r requirements.txt

# 3. Download NLTK data (run once in Python)
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# 4. Start the Flask server
python app.py

# 5. Open frontend/index.html in your browser

API Endpoints
MethodEndpointDescriptionGET/healthCheck server statusPOST/summarize/extractiveTF-IDF summarizationPOST/summarize/abstractiveDistilBART summarizationPOST/summarize/compareBoth methods side by side
Example request:
bashcurl -X POST http://localhost:5000/summarize/extractive \
  -H "Content-Type: application/json" \
  -d '{"text": "Your long text here...", "num_sentences": 3}'
Example response:
json{
  "summary": "Generated summary text.",
  "method": "Extractive (TFIDF)",
  "original_word_count": 320,
  "summary_word_count": 64,
  "compression_ratio": "80.0%"
}
```

---

## How It Works

**Extractive (TF-IDF)** — Cleans and tokenizes the text, computes TF-IDF scores for every word, scores each sentence as the sum of its word scores, then returns the top-N sentences in original order.

**Abstractive (DistilBART)** — Tokenizes input into subword tokens, passes them through the transformer encoder to create contextual embeddings, generates a new summary token by token via beam search decoding.

**Compression Ratio** — `(1 − Summary Words / Original Words) × 100%`

---

## Dependencies
```
flask==3.0.0
flask-cors==4.0.0
nltk==3.8.1
scikit-learn==1.3.2
numpy==1.26.2
transformers==4.36.0
torch==2.1.1
sentencepiece==0.1.99

Notes

Abstractive model downloads ~500MB on first run, then caches locally
Texts over 700 words are auto-truncated before abstractive processing
Extractive mode works fully offline with no model download
Minimum input: 30 words (extractive) / 50 words (abstractive)


Future Improvements

ROUGE score evaluation
PDF and file upload support
Multilingual summarization (mBART)
BERT-based sentence scoring
Keyword extraction feature
