import streamlit as st

# NLP Libraries
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import re

# App Title and Input Area
st.title("NLP Sentiment Analysis App")
st.subheader("Enter text below to analyze its sentiment")
text_input = st.text_area("Your text here:")

# Analyze button
if st.button("Analyze"):
    # Step 1: Clean the text
    text = re.sub(r"[^A-Za-z0-9]+", " ", text_input)         # Keep only text and digits
    text = re.sub("\s+", " ", text)                          # Remove extra whitespaces
    text = re.sub("http\S+", " link ", text)                 # Remove links
    text = re.sub("\d+(\.\d+)?", "", text)                   # Remove numbers
    text = text.split()                                      # Split into tokens

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
    cleaned_text = " ".join(lemmatized_words)

    # Step 2: Sentiment Analysis
    blob = TextBlob(cleaned_text)
    sentiment_score = blob.sentiment.polarity

    # Step 3: Display Result
    if sentiment_score > 0:
        custom_emoji = ':blush:'
        st.success(f"Happy {custom_emoji} | Polarity Score: {sentiment_score}")
    elif sentiment_score < 0:
        custom_emoji = ':disappointed:'
        st.warning(f"Sad {custom_emoji} | Polarity Score: {sentiment_score}")
    else:
        custom_emoji = ':confused:'
        st.info(f"Confused {custom_emoji} | Polarity Score: {sentiment_score}")