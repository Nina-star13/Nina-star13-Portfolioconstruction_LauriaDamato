import streamlit as st
import pandas as pd

# Configura la pagina
st.set_page_config("Home", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")

# Immagine di copertura
st.image("static/home_image.jpg", use_container_width=True)

# Titolo
st.title("Home")

# Descrizione del sito
st.markdown("""
Welcome! This website offers you the possibility to:

- Access the Crypto section to create an investment portfolio.
- Start with a portfolio consisting of 50% in SPY and 50% in IEF.
- Add ETH, BTC or both to your wallet while maintaining a maximum of 25% overall exposure in cryptocurrencies.

The goal is to provide you with a simple and functional interface for customising your wallet, combining traditional assets and cryptocurrencies.
""")

# Verifica se il file dati è disponibile (come "healthcheck")
try:
    df = pd.read_csv("static/data.csv")
    st.success("Data file loaded successfully. Service is up and running.")
except Exception as e:
    st.error("Service unavailable: failed to load data file.")
