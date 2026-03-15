# summarizer.py
import re
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

class TextRankSummarizer:
    def __init__(self, ratio=0.3):
        self.ratio = ratio
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer()

    def clean_sentence(self, sentence):
        sentence = sentence.lower()
        sentence = re.sub(r'[^a-z\s]', ' ', sentence)
        sentence = re.sub(r'\s+', ' ', sentence).strip()
        words = sentence.split()
        words = [w for w in words if w not in self.stop_words]
        return ' '.join(words)

    def summarize(self, text):
        sentences = sent_tokenize(text)
        if len(sentences) == 0:
            return ""

        cleaned = [self.clean_sentence(s) for s in sentences]
        tfidf_matrix = self.vectorizer.fit_transform(cleaned)
        sim_matrix = cosine_similarity(tfidf_matrix)
        np.fill_diagonal(sim_matrix, 0)

        nx_graph = nx.from_numpy_array(sim_matrix)
        scores = nx.pagerank(nx_graph)
        sentence_scores = [scores[i] for i in range(len(sentences))]

        n_sent = len(sentences)
        n_summary = max(1, int(n_sent * self.ratio))
        sorted_indices = sorted(
            range(n_sent),
            key=lambda i: sentence_scores[i],
            reverse=True
        )
        top_indices = sorted(sorted_indices[:n_summary])
        summary_sentences = [sentences[i] for i in top_indices]
        return ' '.join(summary_sentences)
