import streamlit as st
import joblib


# Load the model
model = joblib.load('twitter_sentiment_analysis_model.pkl')
 
# Load the vectorizer
vectorizer = joblib.load('vectorizer.pkl')

# Title
st.set_page_config(page_title=f"Twitter Sentiment Analysis", page_icon="twitter_pic.png")
st.title(f'Twitter Sentiment Analysis')
st.write('This is a simple web app to predict the sentiment of a tweet using a SVM learning model.')

# Sidebar - Description
st.sidebar.header("About the Sentiment Analysis")
st.sidebar.markdown("""
    **Description:**
    - This application uses a Support Vector Machine (SVM) model to predict the sentiment of a tweet.
    - The sentiment prediction could be **Positive**, **Negative**, or **Neutral** based on the input tweet.
    - The model has been trained on a dataset of tweets, and we use a vectorizer to transform the tweet into a format suitable for the model.
    - **SVM** is a supervised learning algorithm that classifies data by finding a hyperplane that best divides the data into classes.
    - The model predicts the sentiment of a tweet using features extracted from the text data.
""")

tweet = st.text_area('Enter your tweet')
vectorizer_tweet = vectorizer.transform([tweet])
prediction = model.predict(vectorizer_tweet)

if st.button('Predict'):
    if prediction[0] == -1:
        st.error("⚠️ Negative Sentiment detected!")
    elif prediction[0] == 1:
        st.success("✅ Positive Sentiment detected!")
    else:
        st.warning("⚪ Neutral Sentiment detected!")

# Footer
st.markdown("---")

# Contact Information
st.markdown("### 📬 Connect with Me")
st.markdown(
    """
    - 🛠️ [GitHub](https://github.com/RimeshCdry/)  
    - ✉️ Email: rimeshcdry45@gmail.com  
    """
)
