# Stock & Crypto Tracker

A Python project to fetch and visualize financial data using APIs.

## What It Does
- Fetch real-time stock and crypto prices via Yahoo Finance API
- Plot historical price charts with matplotlib
- Compare multiple assets on a single chart (normalized or raw)
- Track portfolio value across stocks and crypto
- Set price alerts for buy/sell signals

## Features

| Level | Feature | Status |
|-------|---------|--------|
| 1 | Fetch and print current price | ✅ |
| 2 | Plot historical prices | ✅ |
| 3 | Compare multiple tickers on one chart | ✅ |
| 4 | Portfolio tracker (holdings + total value) | ✅ |
| 5 | Price alerts | ✅ |
| 6 | Web dashboard | Future |

## APIs Used
- **yfinance** - Yahoo Finance wrapper (stocks, ETFs, crypto)
- **CoinGecko** - Crypto data (optional, for deeper crypto features)

## Setup

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python tracker.py
```

Or import functions in your own scripts:

```python
from tracker import get_current_price, track_portfolio, check_price_alerts

# Get current price
price = get_current_price("AAPL")

# Track portfolio
holdings = {"AAPL": 10, "BTC-USD": 0.5}
portfolio = track_portfolio(holdings)

# Set alerts
alerts = [{"symbol": "AAPL", "target": 200, "direction": "above"}]
triggered = check_price_alerts(alerts)
```

## Resources
- [yfinance docs](https://github.com/ranaroussi/yfinance)
- [CoinGecko API](https://www.coingecko.com/en/api/documentation)
- [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Plotly Python](https://plotly.com/python/)
