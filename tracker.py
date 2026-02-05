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
# LEVEL 4: Portfolio tracker
# =============================================================================

def track_portfolio(holdings: dict) -> dict:
    """
    Track the value of your portfolio.

    Args:
        holdings: dict of {symbol: quantity}
                  e.g., {"AAPL": 10, "BTC-USD": 0.5, "MSFT": 25}

    Returns:
        dict with portfolio breakdown and total value
    """
    portfolio = []
    total_value = 0

    for symbol, quantity in holdings.items():
        data = get_current_price(symbol)
        if data["price"] is None:
            print(f"  Warning: Could not fetch price for {symbol}")
            continue

        value = data["price"] * quantity
        total_value += value

        portfolio.append({
            "symbol": symbol,
            "name": data["name"],
            "quantity": quantity,
            "price": data["price"],
            "value": value,
            "currency": data["currency"],
        })

    return {
        "holdings": portfolio,
        "total_value": total_value,
    }


def print_portfolio(holdings: dict):
    """Print a formatted portfolio summary."""
    result = track_portfolio(holdings)

    print(f"{'Symbol':<12} {'Name':<20} {'Qty':>10} {'Price':>12} {'Value':>14}")
    print("-" * 70)

    for h in result["holdings"]:
        print(f"{h['symbol']:<12} {h['name'][:20]:<20} {h['quantity']:>10.4g} "
              f"${h['price']:>10,.2f} ${h['value']:>12,.2f}")

    print("-" * 70)
    print(f"{'TOTAL':<44} ${result['total_value']:>26,.2f}")


# =============================================================================
# LEVEL 5: Price alerts
# =============================================================================

def check_price_alerts(alerts: list) -> list:
    """
    Check if any price alerts have been triggered.

    Args:
        alerts: list of dicts, each with:
                - symbol: ticker symbol
                - target: target price
                - direction: "above" or "below"

    Returns:
        list of triggered alerts with current prices
    """
    triggered = []

    for alert in alerts:
        symbol = alert["symbol"]
        target = alert["target"]
        direction = alert["direction"]

        data = get_current_price(symbol)
        if data["price"] is None:
            continue

        current = data["price"]
        is_triggered = (
            (direction == "above" and current >= target) or
            (direction == "below" and current <= target)
        )

        if is_triggered:
            triggered.append({
                "symbol": symbol,
                "name": data["name"],
                "target": target,
                "current": current,
                "direction": direction,
            })

    return triggered


def print_alerts(alerts: list):
    """Check alerts and print any that are triggered."""
    triggered = check_price_alerts(alerts)

    if not triggered:
        print("No alerts triggered.")
        return

    print(f"{'Symbol':<12} {'Alert':<20} {'Current':>12} {'Target':>12}")
    print("-" * 58)

    for a in triggered:
        alert_type = f"Price {a['direction']} target"
        print(f"{a['symbol']:<12} {alert_type:<20} ${a['current']:>10,.2f} ${a['target']:>10,.2f}")


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


    # --- LEVEL 4: Uncomment to try ---
    # print("\n=== Level 4: Portfolio Tracker ===\n")
    # my_holdings = {
    #     "AAPL": 10,      # 10 shares of Apple
    #     "MSFT": 5,       # 5 shares of Microsoft
    #     "BTC-USD": 0.5,  # 0.5 Bitcoin
    # }
    # print_portfolio(my_holdings)


    # --- LEVEL 5: Uncomment to try ---
    # print("\n=== Level 5: Price Alerts ===\n")
    # my_alerts = [
    #     {"symbol": "AAPL", "target": 200, "direction": "above"},
    #     {"symbol": "BTC-USD", "target": 100000, "direction": "above"},
    #     {"symbol": "TSLA", "target": 300, "direction": "below"},
    # ]
    # print_alerts(my_alerts)
