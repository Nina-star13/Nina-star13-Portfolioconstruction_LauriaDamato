**Crypto Portfolio Dashboard**
This project provides a cryptocurrency portfolio dashboard built using Streamlit. The application allows users to:
- View real-time cryptocurrency data (Bitcoin and Ethereum).
- Create a portfolio with a 50% allocation in SPY and 50% in IEF, with the option to add up to 25% in cryptocurrencies.
- Visualize portfolio performance (returns, volatility, Sharpe ratio, kurtosis, and skewness).
- Download portfolio data in CSV format.

**Features**
- Real-time Data: Fetches live data for Bitcoin and Ethereum from Yahoo Finance.
- Portfolio Management: Allows users to create and customize their portfolios, integrating cryptocurrencies.
- Performance Metrics: Displays key financial metrics including returns, volatility, Sharpe ratio, kurtosis, and skewness.
- Data Export: Users can download portfolio data as a CSV file.

**Requirements**
- Python 3.x
- streamlit
- pandas
- yfinance
- plotly
- httpx

**Installation**
- Copy this repository:
  git clone https://github.com/yourusername/crypto-dashboard.git
  cd crypto-dashboard

- Install the required dependencies:
  pip install -r requirements.txt

- Run the Streamlit app:
  streamlit run Home.py
