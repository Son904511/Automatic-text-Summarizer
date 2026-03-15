# app.py
import streamlit as st
from summarizer import TextRankSummarizer

st.title("Automatic Text Summarizer (TextRank)")

st.write("Paste any long English text below and click Summarize.")

# Slider to control summary ratio
ratio = st.slider("Summary length (percentage of original sentences)",
                  min_value=10, max_value=80, value=30, step=5)

text = st.text_area("Input text:", height=250)

if st.button("Summarize"):
    if not text.strip():
        st.warning("Please paste some text first.")
    else:
        summarizer = TextRankSummarizer(ratio=ratio/100.0)
        summary = summarizer.summarize(text)

        st.subheader("Summary:")
        st.write(summary)

        st.subheader("Stats:")
        st.write(f"Summary ratio: {ratio}% of original sentences")
