import streamlit as st
import joblib

# Load saved model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Page title
st.title("Fake News Detection System")

st.write("Enter news text and topic to check if it is Fake or Real.")

# Input fields
news_text = st.text_area("Enter News Text")
news_topic = st.text_input("Enter Topic")

# Prediction button
if st.button("Check News"):

    if news_text and news_topic:

        content = news_text + " " + news_topic

        vector = vectorizer.transform([content])

        prediction = model.predict(vector)

        if prediction[0] == 0:
            st.error("⚠️ This looks like Fake News")
        else:
            st.success("✅ This looks like Real News")

    else:
        st.warning("Please enter both text and topic.")