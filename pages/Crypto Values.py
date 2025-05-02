import streamlit as st
import pandas as pd
import plotly.express as px

# Configurazione della pagina
st.set_page_config("Crypto Values", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")
st.title("Daily Cryptocurrency Data")

# Caricamento del file CSV locale
df = pd.read_csv("static/data.csv", parse_dates=["date"])
df.set_index("date", inplace=True)

# Seleziona solo le colonne di interesse
crypto_df = df[["BTC-USD", "ETH-USD"]].copy()
crypto_df.columns = ["Bitcoin (BTC)", "Ethereum (ETH)"]

# Controllo presenza dati
if crypto_df.dropna().empty:
    st.warning("No crypto data available in data.csv.")
else:
    # Visualizzazione dei dati in tabella
    st.subheader("Price table")
    st.dataframe(crypto_df.style.format("{:.2f}"), use_container_width=True)

    # Creazione del grafico interattivo
    st.subheader("Price trends")
    fig = px.line(
        crypto_df,
        x=crypto_df.index,
        y=crypto_df.columns,
        labels={"value": "Price (USD)", "variable": "Cryptocurrency"},
        title="Price trends for BTC and ETH"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Pulsante per il download dei dati in formato CSV
    csv = crypto_df.reset_index().to_csv(index=False)
    st.download_button(
        label="Download crypto data in CSV",
        data=csv,
        file_name="crypto_data.csv",
        mime="text/csv"
    )
