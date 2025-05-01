import streamlit as st
import pandas as pd
import plotly.express as px
from scipy.stats import skew, kurtosis

st.set_page_config("Crypto", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")

st.title("Portfolio construction")

# Caricamento dati
df = pd.read_csv("static/data.csv", parse_dates=["date"])
df.set_index("date", inplace=True)

# Selezione crypto
st.sidebar.markdown("### Select Cryptocurrencies to add")
selected_crypto = st.sidebar.multiselect(
    "You can choose a maximum of two cryptocurrencies:", options=["BTC-USD", "ETH-USD"], max_selections=2
)

# Input percentuale crypto
max_crypto_pct = 25  # massimo consentito
crypto_pct = 0
if selected_crypto:
    crypto_pct = st.sidebar.slider(
        "Total percentage to be allocated in crypto", min_value=5, max_value=25, step=5, value=10
    )

# Costruzione portafoglio
weights = {"SPY": 0.5, "IEF": 0.5}
if selected_crypto:
    remaining = 1 - crypto_pct / 100
    weights["SPY"] = round(weights["SPY"] * remaining, 4)
    weights["IEF"] = round(weights["IEF"] * remaining, 4)
    equal_crypto_weight = round((crypto_pct / 100) / len(selected_crypto), 4)
    for crypto in selected_crypto:
        weights[crypto] = equal_crypto_weight

# Visualizzazione tabella pesi
st.subheader("Portfolio allocation")
weights_df = pd.DataFrame.from_dict(weights, orient="index", columns=["Weight"])
weights_df["%"] = weights_df["Weight"] * 100
st.dataframe(weights_df.style.format({"Weight": "{:.2%}", "%": "{:.1f}"}))

# Grafico a torta
fig = px.pie(
    names=weights_df.index,
    values=weights_df["Weight"],
    title="Portfolio Distribution",
    color_discrete_sequence=px.colors.sequential.RdBu
)
st.plotly_chart(fig)

# Calcolo valore cumulativo portafoglio
portfolio_prices = df[list(weights.keys())]
normalized_prices = portfolio_prices / portfolio_prices.iloc[0]
portfolio_value = (normalized_prices * list(weights.values())).sum(axis=1)

st.subheader("Historical portfolio performance")
fig_value = px.line(portfolio_value, title="Normalised portfolio value")
st.plotly_chart(fig_value)

# Calcolo delle performance
returns = portfolio_value.pct_change().dropna()
mean_return = returns.mean()
volatility = returns.std() * (252 ** 0.5)  # annualizzata
sharpe_ratio = mean_return / returns.std() * (252 ** 0.5)  # risk-free = 0
skewness = skew(returns)
kurt = kurtosis(returns)

st.subheader("Portfolio performance")
st.write(f"**Average daily return**: {mean_return:.4%}")
st.write(f"**Annualised volatility**: {volatility:.2%}")
st.write(f"**Sharpe Ratio**: {sharpe_ratio:.2f}")
st.write(f"**Skewness**: {skewness:.2f}")
st.write(f"**Kurtosis**: {kurt:.2f}")

# Download del portafoglio
st.subheader("Download portfolio composition")
csv = weights_df.reset_index().rename(columns={"index": "Asset"}).to_csv(index=False)
st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="portafoglio.csv",
    mime="text/csv"
)

