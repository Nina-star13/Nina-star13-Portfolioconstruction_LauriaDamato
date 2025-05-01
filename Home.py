import streamlit as st
import httpx
# run  streamlit run Home.py in the terminal

def healthcheck(): #Make sure the server works
    response = httpx.get("http://127.0.0.1:8000/health")
    return response.is_success

st.set_page_config("Home", page_icon="static/favicon-32x32.png") # configure page with link title and icon 
st.logo("static/uniupo-logo.svg", size="large")

# Aggiungi un logo o un'immagine di copertura nella pagina
st.image("static/home_image.jpg", use_container_width=True)

st.title("Home")

# Descrizione del sito
st.markdown("""
Welcome! This website offers you the possibility to:

- Access the Crypto section to create an investment portfolio.
- Start with a portfolio consisting of 50% in SPY and 50% in IEF.
- Add ETH, BTC or both to your wallet while maintaining a maximum of 25% overall exposure in cryptocurrencies.

The goal is to provide you with a simple and functional interface for customising your wallet, combining traditional assets and cryptocurrencies.
""")

if healthcheck():
    st.success("Service is up and running")
else:
    st.error("Service unavailable")