# Stock & Crypto Tracker

A web dashboard to track stocks and crypto prices, visualize charts, and monitor your portfolio.

**[Live Demo](https://cblythe8-stock-crypto-tracker.streamlit.app)** (https://stock-crypto-tracker-vt6hb433hctduebdcvcnzr.streamlit.app/)

## Features

- **Price Lookup** - Real-time stock and crypto prices
- **Price Charts** - Historical price visualization
- **Compare Assets** - Side-by-side comparison with normalized % change
- **Portfolio Tracker** - Track your holdings and total value
- **Price Alerts** - Get notified when assets hit target prices

## Quick Start

### Run Locally

```bash
# Clone the repo
git clone https://github.com/cblythe8/Stock-Crypto-Tracker.git
cd Stock-Crypto-Tracker

# Install dependencies
pip install -r requirements.txt

# Run the web app
streamlit run app.py
```

### Command Line Version

```bash
python tracker.py
```

## Tech Stack

- **Python** - Core language
- **yfinance** - Yahoo Finance API wrapper
- **Streamlit** - Web dashboard framework
- **Pandas** - Data manipulation
- **Matplotlib** - Charts (CLI version)

## Supported Symbols

| Type | Examples |
|------|----------|
| Stocks | AAPL, GOOGL, MSFT, TSLA, AMZN |
| Crypto | BTC-USD, ETH-USD, SOL-USD |
| ETFs | SPY, QQQ, VOO |
