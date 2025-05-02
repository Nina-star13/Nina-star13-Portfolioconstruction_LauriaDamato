import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# Configura la pagina
st.set_page_config("Data", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")
st.title("Daily Cryptocurrency Real-Time Data")

# Tickers da Yahoo Finance
tickers = ["BTC-USD", "ETH-USD"]

# Scarica dati storici
try:
    data = yf.download(tickers=tickers, period="1y", interval="1d")["Close"]
    if data.empty:
        st.error("⚠️ No data was returned from Yahoo Finance. Please try again later.")
    else:
        # Rinomina colonne
        data.columns = ["Bitcoin (BTC)", "Ethereum (ETH)"]
        data.index.name = "Date"

        # Mostra tabella
        st.subheader("Price Table")
        st.dataframe(data.style.format("{:.2f}"), use_container_width=True)

        # Converte in formato long per plotly
        df_long = data.reset_index().melt(id_vars="Date", var_name="Cryptocurrency", value_name="Price")

        # Crea grafico
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

        # Pulsante download CSV
        csv = data.reset_index().to_csv(index=False)
        st.download_button(
            label="Download Crypto Data as CSV",
            data=csv,
            file_name="crypto_data.csv",
            mime="text/csv"
        )

except Exception as e:
    st.error(f"An error occurred while downloading data: {e}")


