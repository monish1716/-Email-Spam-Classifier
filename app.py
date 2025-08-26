import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# Ensure stopwords are available at runtime
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", quiet=True)

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = text.split()

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load model + vectorizer
tfidf_vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

# Streamlit UI
st.title("Email Spam Classifier")
input_sms = st.text_area("Enter the content of the email below to classify it as Spam or Not Spam.")

if st.button("Predict"):
    # 1. preprocess the input
    transformed_sms = transform_text(input_sms)
    # 2. vectorize the input
    vector_input = tfidf_vectorizer.transform([transformed_sms])
    # 3. predict the input
    result = model.predict(vector_input)[0]
    # 4. display the result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
