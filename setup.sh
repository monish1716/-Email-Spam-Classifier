mkdir -p ~/.streamlit/

echo "\
[general]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
"> ~/.streamlit/config.toml

# Download NLTK data before running the app
python3 -m nltk.downloader punkt
nltk.download('punkt_tab')
python3 -m nltk.downloader stopwords

