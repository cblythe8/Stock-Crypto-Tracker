"""
Stock & Crypto Tracker
======================
A simple tool to fetch and visualize financial data.

Start with Level 1, then uncomment sections as you progress!
"""

import yfinance as yf
import matplotlib.pyplot as plt


# =============================================================================
# LEVEL 1: Fetch and print current price
# =============================================================================

def get_current_price(symbol: str) -> dict:
    """Fetch current price info for a stock/crypto."""
    ticker = yf.Ticker(symbol)
    info = ticker.info

    return {
        "symbol": symbol,
        "name": info.get("shortName", "Unknown"),
        "price": info.get("currentPrice") or info.get("regularMarketPrice"),
        "currency": info.get("currency", "USD"),
    }


# =============================================================================
# LEVEL 2: Plot historical prices
# =============================================================================

def plot_history(symbol: str, period: str = "1mo"):
    """
    Plot historical closing prices.

    Periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    """
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period=period)

    plt.figure(figsize=(10, 6))
    plt.plot(hist.index, hist["Close"], label=symbol)
    plt.title(f"{symbol} - Last {period}")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# =============================================================================
# LEVEL 3: Compare multiple tickers
# =============================================================================

def compare_tickers(symbols: list, period: str = "1mo", normalize: bool = True):
    """
    Compare multiple stocks/cryptos on one chart.

    Set normalize=True to show percentage change (easier to compare).
    """
    plt.figure(figsize=(12, 6))

    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period)

        if normalize:
            # Convert to percentage change from start
            prices = (hist["Close"] / hist["Close"].iloc[0] - 1) * 100
            plt.ylabel("Change (%)")
        else:
            prices = hist["Close"]
            plt.ylabel("Price ($)")

        plt.plot(hist.index, prices, label=symbol)

    plt.title(f"Comparison - Last {period}")
    plt.xlabel("Date")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# =============================================================================
# MAIN - Uncomment sections as you progress through levels
# =============================================================================

if __name__ == "__main__":

    # --- LEVEL 1: Try these ---
    print("=== Level 1: Current Prices ===\n")

    # Try different symbols: AAPL, GOOGL, MSFT, TSLA, BTC-USD, ETH-USD
    stock = get_current_price("AAPL")
    print(f"{stock['name']} ({stock['symbol']})")
    print(f"  Price: ${stock['price']:.2f} {stock['currency']}")
    print()

    crypto = get_current_price("BTC-USD")
    print(f"{crypto['name']} ({crypto['symbol']})")
    print(f"  Price: ${crypto['price']:,.2f} {crypto['currency']}")


    # --- LEVEL 2: Uncomment to try ---
    # print("\n=== Level 2: Historical Chart ===\n")
    # plot_history("AAPL", period="3mo")


    # --- LEVEL 3: Uncomment to try ---
    # print("\n=== Level 3: Compare Tickers ===\n")
    # compare_tickers(["AAPL", "GOOGL", "MSFT"], period="6mo", normalize=True)
    # compare_tickers(["BTC-USD", "ETH-USD"], period="3mo", normalize=True)
