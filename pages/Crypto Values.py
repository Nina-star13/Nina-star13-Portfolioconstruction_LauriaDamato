import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# Configurazione della pagina
st.set_page_config("Data", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")
st.title("Daily Cryptocurrency real time data")

# Definizione dei ticker delle criptovalute
tickers = ["BTC-USD", "ETH-USD"]

# Download dei dati storici per l'ultimo anno
df = yf.download(tickers=tickers, period="1y", interval="1d")["Close"]

# Rinomina delle colonne per una migliore leggibilità
df.columns = ["Bitcoin (BTC)", "Ethereum (ETH)"]

# Visualizzazione dei dati in tabella
st.subheader("Price table")
st.dataframe(df.style.format("{:.2f}"), use_container_width=True)

# Creazione del grafico interattivo
st.subheader("Price trends")
fig = px.line(df, x=df.index, y=df.columns, labels={"value": "Price (USD)", "variable": "Criptovalue"}, title="Price trends for BTC and ETH")
st.plotly_chart(fig, use_container_width=True)

# Pulsante per il download dei dati in formato CSV
csv = df.reset_index().to_csv(index=False)
st.download_button(
    label="Download crypto data in CSV",
    data=csv,
    file_name="crypto_dati.csv",
    mime="text/csv"
)




