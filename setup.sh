mkdir -p ~/.streamlit/

echo "\
[general]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
"> ~/.streamlit/config.toml

python3 generate_data.py