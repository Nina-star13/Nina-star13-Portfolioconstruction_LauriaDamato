import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# Configurazione della pagina
st.set_page_config("Data", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")
st.title("Daily Cryptocurrency Real-Time Data")

# Definizione dei ticker delle criptovalute
tickers = ["BTC-USD", "ETH-USD"]

# Download dei dati storici per l'ultimo anno
df = yf.download(tickers=tickers, period="1y", interval="1d")["Close"]

# Rinomina delle colonne per una migliore leggibilità
df.columns = ["Bitcoin (BTC)", "Ethereum (ETH)"]
df.index.name = "Date"

# Visualizzazione dei dati in tabella
st.subheader("Price Table")
st.dataframe(df.style.format("{:.2f}"), use_container_width=True)

# Conversione dei dati in formato "long" per Plotly
df_long = df.reset_index().melt(id_vars="Date", var_name="Cryptocurrency", value_name="Price")

# Creazione del grafico interattivo
st.subheader("Price Trends")
fig = px.line(
    df_long,
    x="Date",
    y="Price",
    color="Cryptocurrency",
    labels={"Price": "Price (USD)", "Cryptocurrency": "Cryptocurrency"},
    title="Price Trends for BTC and ETH"
)
st.plotly_chart(fig, use_container_width=True)

# Pulsante per il download dei dati in formato CSV
csv = df.reset_index().to_csv(index=False)
st.download_button(
    label="Download Crypto Data as CSV",
    data=csv,
    file_name="crypto_data.csv",
    mime="text/csv"
)



