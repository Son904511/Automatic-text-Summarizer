import re
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

nltk.download('punkt')
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

if __name__ == "__main__":
    text = """
    By: Express Global Desk
6 min readMar 8, 2026 09:30 AM IST
iran-israel war - flight status ops uae Air India air india expressA stranded passenger sleeps on the floor outside Dubai International Airport terminal as the airport resumes limited operations in Dubai, United Arab Emirates, Thursday, March 5, 2026. (AP Photo)
Make us preferred source on Google


Print

Hundreds of passengers remain stranded across the Middle East amid the ongoing conflict involving the United States, Israel and Iran, which has disrupted travel across parts of the Gulf region. Authorities and airlines are now making efforts to bring affected nationals back home.

Air India, Air India Express
With airspace over Saudi Arabia and Oman remaining open, Air India and Air India Express said on March 8 that they will continue operating flights to and from Jeddah and Muscat, which have been assessed as safe for operations.

“Air India is maintaining scheduled flights from Delhi and Mumbai to Jeddah and back. Air India Express continues scheduled operations connecting Muscat with Delhi, Kochi, Kozhikode, Mangaluru, Mumbai and Kannur, as well as services between Jeddah and Bengaluru, Kozhikode and Mangaluru,” the airlines said.

The carriers also announced that additional non-scheduled flights will operate on March 8 to and from Abu Dhabi, Dubai, Muscat, Ras Al Khaimah and Sharjah to bring stranded passengers back to India. Since these flights are intended primarily for stranded travellers, priority will be given to passengers holding existing bookings with either airline.

Air India’s additional flights will operate from Delhi and Mumbai to Dubai and back, while Air India Express will run 30 extra flights between India and UAE cities including Abu Dhabi, Dubai, Ras Al Khaimah and Sharjah.


In a post on X, the airlines said that flight timings and schedules may change due to the evolving conflict situation in West Asia. Passengers have been advised to verify their flight status before heading to the airport.

Air India also said that its flights to Europe and North America are operating normally through safe alternative routings.

The following scheduled flights are planned to operate on 8th March 2026: 

The following scheduled flights are planned to operate on 8th March 2026: The scheduled flights that are planned to operate on 8th March 2026
Non-scheduled flights are planned for 8 March The non-scheduled flights that are planned for 8 March
The airlines further advised passengers requiring rebooking or cancellation to submit requests through the Air India website. For assistance, travellers can contact the airline’s 24×7 customer support at +91-11-69329333 or +91-11-69329999.

Air India Express passengers departing from any station in the UAE can also rebook their flights without additional charges on the airline’s extra commercial services operating from UAE cities to destinations across India.

Etihad Airways
According to its latest advisory, Etihad Airways will continue operating a limited commercial flight schedule from March 6, 2026, with services running between Abu Dhabi and several global destinations.

The airline said priority will be given to passengers holding existing bookings and advised travellers to check their flight status before heading to the airport.

The following destinations are scheduled to operate to and from Abu Dhabi between March 6 and March 19:

Ahmedabad, Addis Ababa, Amsterdam, Athens, Atlanta, Bangkok, Barcelona, Beijing, Bengaluru, Boston, Brussels, Cairo, Casablanca, Chiang Mai, Chicago, Colombo, Copenhagen, Delhi, Denpasar (Bali), Dublin, Düsseldorf, Frankfurt, Geneva, Hanoi, Hong Kong, Hyderabad, Islamabad, Istanbul, Jakarta, Jeddah, Karachi, Kochi, Kolkata, Kozhikode, Krabi, Kuala Lumpur, Lahore, London (Heathrow), Madrid, Malé, Manchester, Manila, Medina, Melbourne, Milan (Malpensa), Moscow (Sheremetyevo), Mumbai, Munich, Muscat, Nairobi, New York (JFK), Paris, Phnom Penh, Phuket, Prague, Riyadh, Rome, Seoul (Incheon), Seychelles, Singapore, St Petersburg, Sydney, Taipei, Thiruvananthapuram, Tokyo, Toronto, Vienna, Warsaw, Washington and Zurich.
    """

    summarizer = TextRankSummarizer(ratio=0.3)
    summary = summarizer.summarize(text)

    print("ORIGINAL TEXT:\n")
    print(text)
    print("\nSUMMARY:\n")
    print(summary)
