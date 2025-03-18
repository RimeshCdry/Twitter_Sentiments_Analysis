# Twitter Sentiment Analysis using SVM 🌟

## Overview 📄

This project performs sentiment analysis on tweets using the **Support Vector Machine (SVM)** model. The pipeline includes data collection, **data preprocessing**, **cleaning the text**, **removing stopwords**, **Porter Stemming**, **vectorization** of text data, **splitting data** into training and testing sets, and **model evaluation**. Additionally, a **web application** using **Streamlit** has been developed to interact with the model for real-time sentiment predictions.

---

## Project Workflow 🔄

### 1. Data Collection 📂
  - Collected tweet data using kaggle.

### 2. Text Preprocessing 🔍
- **Text Cleaning**: Removed noise like URLs, user mentions, hashtags, and punctuation.
- **Stopwords Removal**: Removed common words that don’t add value to sentiment analysis.
- **Porter Stemming**: Applied stemming to reduce words to their root form.

### 3. Text Vectorization 📊
- **TfidfVectorizer** was used to convert text data into numerical format, making it suitable for model training.

### 4. Train-Test Split 🔢
- Split the dataset into **training** and **testing** sets for model training and evaluation.

### 5. Model Training 🤖
- Trained the **SVM model** using **Scikit-learn** with the training data.
- The SVM classifier was tuned to predict tweet sentiment (positive, negative, neutral).

### 6. Model Evaluation 📊
- Evaluated the model's performance using **accuracy**, **precision**, **recall**, and **F1-score**.

### 7. Real-Time Prediction 🔮
- Built a **Streamlit web application** where users can input tweets and get sentiment predictions.

---

## UI Development 🖥️
- A **Graphical User Interface** was developed using **Streamlit**.
- Users can enter a tweet and receive the sentiment prediction instantly.

---

## Technologies Used 💻
- **Python** (Pandas, NumPy, re, Scikit-learn, NLTK)
- **Streamlit** (for UI)
- **Jupyter Notebook** (for model training and evaluation)

---

## Installation Guide 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/twitter-sentiment-svm.git
   cd twitter-sentiment-svm
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Stramlit UI:
   ```bash
   streamlit run app.py
   ```

---

## User Guide🚀:
  - Open the Streamlit UI in a browser.
  - Enter a tweet in the input box for sentiment prediction.
  - View the sentiment of the tweets.

---

## Results & Insights📊
  - The SVM model performs well in identifying sentiments in tweets.
  - The UI provides an interactive way to predict sentiment for any given tweet.
  - This can be useful for social media analysis, brand monitoring, and customer feedback analysis.

---

## 👥 Contact
For questions or feedback, feel free to reach out:
  - GitHub: [@RimeshCdry](https://github.com/RimeshCdry)
  - Email: rimeshcdry45@gmail.com
  - Linkedin: https://www.linkedin.com/in/rimesh-chaudhary-09a25a30a
