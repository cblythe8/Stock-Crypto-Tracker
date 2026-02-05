# Stock & Crypto Tracker

A Python project to fetch and visualize financial data using APIs.

## Learning Goals
- [ ] Understand how APIs work (requests, responses, JSON)
- [ ] Fetch real-time and historical price data
- [ ] Use pandas for data manipulation
- [ ] Create visualizations with matplotlib/plotly
- [ ] Build a portfolio tracker

## Project Levels

| Level | Goal | Status |
|-------|------|--------|
| 1 | Fetch and print current price | |
| 2 | Plot historical prices (30 days) | |
| 3 | Compare multiple tickers on one chart | |
| 4 | Portfolio tracker (holdings + total value) | |
| 5 | Price alerts | |
| 6 | Web dashboard | |

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

## Resources
- [yfinance docs](https://github.com/ranaroussi/yfinance)
- [CoinGecko API](https://www.coingecko.com/en/api/documentation)
- [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Plotly Python](https://plotly.com/python/)
