🧠 NLP Text Summarizer (Extractive + Abstractive)

An NLP-based web application that summarizes long text using both Extractive and Abstractive techniques.
The application allows side-by-side comparison of summaries and displays compression ratio metrics to measure summarization efficiency.

This project demonstrates the use of traditional NLP (TF-IDF) and modern Transformer models (DistilBART) in a single application.

🚀 Features

✂️ Extractive Summarization

Uses TF-IDF and word frequency scoring

Selects the most important sentences from the original text

🤖 Abstractive Summarization

Uses DistilBART Transformer

Generates a new human-like summary

📊 Side-by-Side Comparison

Compare extractive and abstractive results

📉 Compression Ratio Metrics

Shows how much the text was reduced

🌐 Simple Web Interface

Lightweight frontend with HTML, CSS, and JavaScript

🏗️ Tech Stack
Layer	Technology
Language	Python 3.10+
Backend	Flask (REST API)
Frontend	HTML, CSS, JavaScript
NLP Libraries	NLTK, Scikit-learn
Deep Learning	HuggingFace Transformers
Model	sshleifer/distilbart-cnn-12-6
Framework	PyTorch
📂 Project Structure
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
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
2️⃣ Install dependencies
cd backend
pip install -r requirements.txt
3️⃣ Download required NLTK data

Run this once in Python:

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
4️⃣ Start the Flask server
python app.py
5️⃣ Run the frontend

Open the file below in your browser:

frontend/index.html
🔗 API Endpoints
Method	Endpoint	Description
GET	/health	Check server status
POST	/summarize/extractive	TF-IDF summarization
POST	/summarize/abstractive	DistilBART summarization
POST	/summarize/compare	Compare both methods
📡 Example API Request
curl -X POST http://localhost:5000/summarize/extractive \
-H "Content-Type: application/json" \
-d '{"text": "Your long text here...", "num_sentences": 3}'
📥 Example Response
{
  "summary": "Generated summary text.",
  "method": "Extractive (TFIDF)",
  "original_word_count": 320,
  "summary_word_count": 64,
  "compression_ratio": "80.0%"
}
⚙️ How It Works
1️⃣ Extractive Summarization (TF-IDF)

Clean and tokenize the input text

Compute TF-IDF scores for words

Score each sentence using the sum of word scores

Select the top N sentences

Return them in the original order

2️⃣ Abstractive Summarization (DistilBART)

Tokenize input into subword tokens

Pass tokens through the Transformer encoder

Generate contextual embeddings

Produce a new summary token-by-token using beam search decoding

3️⃣ Compression Ratio
𝐶
𝑜
𝑚
𝑝
𝑟
𝑒
𝑠
𝑠
𝑖
𝑜
𝑛
 
𝑅
𝑎
𝑡
𝑖
𝑜
=
(
1
−
𝑆
𝑢
𝑚
𝑚
𝑎
𝑟
𝑦
 
𝑊
𝑜
𝑟
𝑑
𝑠
𝑂
𝑟
𝑖
𝑔
𝑖
𝑛
𝑎
𝑙
 
𝑊
𝑜
𝑟
𝑑
𝑠
)
×
100
Compression Ratio=(1−
Original Words
Summary Words
	​

)×100

This metric shows how much the original text was reduced.

📦 Dependencies
flask==3.0.0
flask-cors==4.0.0
nltk==3.8.1
scikit-learn==1.3.2
numpy==1.26.2
transformers==4.36.0
torch==2.1.1
sentencepiece==0.1.99
⚠️ Notes

The abstractive model downloads ~500MB on first run and caches locally.

Texts over 700 words are automatically truncated for abstractive summarization.

Extractive summarization works fully offline.

Minimum input:

30 words → Extractive

50 words → Abstractive

🔮 Future Improvements

📊 ROUGE score evaluation

📄 PDF & document upload

🌍 Multilingual summarization (mBART)

🧠 BERT-based sentence scoring

🔑 Keyword extraction

🖥️ Better UI with summary visualization
