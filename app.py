"""
Stock & Crypto Tracker - Web Dashboard
Built with Streamlit
"""

import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="Stock & Crypto Tracker",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock & Crypto Tracker")
st.markdown("Real-time prices, charts, and portfolio tracking")

# Sidebar for navigation
page = st.sidebar.selectbox(
    "Choose a feature",
    ["Price Lookup", "Price Chart", "Compare Assets", "Portfolio Tracker", "Price Alerts"]
)


def get_price(symbol: str) -> dict:
    """Fetch current price for a symbol."""
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        return {
            "symbol": symbol.upper(),
            "name": info.get("shortName", "Unknown"),
            "price": info.get("currentPrice") or info.get("regularMarketPrice"),
            "currency": info.get("currency", "USD"),
            "change": info.get("regularMarketChangePercent", 0),
        }
    except Exception as e:
        return None


# =============================================================================
# Page: Price Lookup
# =============================================================================
if page == "Price Lookup":
    st.header("💵 Price Lookup")

    col1, col2 = st.columns([2, 3])

    with col1:
        symbol = st.text_input("Enter symbol", value="AAPL", placeholder="AAPL, BTC-USD, ETH-USD...")

        if st.button("Get Price", type="primary"):
            with st.spinner("Fetching..."):
                data = get_price(symbol)

            if data and data["price"]:
                change_color = "green" if data["change"] >= 0 else "red"
                change_symbol = "+" if data["change"] >= 0 else ""

                st.metric(
                    label=f"{data['name']} ({data['symbol']})",
                    value=f"${data['price']:,.2f}",
                    delta=f"{change_symbol}{data['change']:.2f}%"
                )
            else:
                st.error(f"Could not fetch price for '{symbol}'. Check the symbol and try again.")

    with col2:
        st.markdown("### Popular Symbols")
        st.markdown("""
        | Type | Examples |
        |------|----------|
        | Stocks | AAPL, GOOGL, MSFT, TSLA, AMZN |
        | Crypto | BTC-USD, ETH-USD, SOL-USD |
        | ETFs | SPY, QQQ, VOO |
        """)


# =============================================================================
# Page: Price Chart
# =============================================================================
elif page == "Price Chart":
    st.header("📊 Price Chart")

    symbol = st.text_input("Symbol", value="AAPL")

    # Trading mode selection
    mode = st.radio("Chart Mode", ["Day Trading", "Long Term"], horizontal=True)

    if mode == "Day Trading":
        col1, col2 = st.columns(2)
        with col1:
            interval = st.selectbox("Interval", ["1m", "5m", "15m", "30m", "1h"], index=1)
        with col2:
            period = st.selectbox("Period", ["1d", "5d", "7d"], index=0)
        st.caption("Intraday data limited to last 7 days for minute intervals, 60 days for hourly")
    else:
        col1, col2 = st.columns(2)
        with col1:
            interval = "1d"
            period = st.selectbox("Period", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], index=2)
        with col2:
            st.write("")  # Spacer

    if st.button("Show Chart", type="primary"):
        with st.spinner("Loading chart..."):
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period, interval=interval)

        if not hist.empty:
            st.line_chart(hist["Close"])

            col1, col2, col3 = st.columns(3)
            col1.metric("Current", f"${hist['Close'].iloc[-1]:,.2f}")
            col2.metric("Period High", f"${hist['Close'].max():,.2f}")
            col3.metric("Period Low", f"${hist['Close'].min():,.2f}")
        else:
            st.error(f"No data found for '{symbol}'")


# =============================================================================
# Page: Compare Assets
# =============================================================================
elif page == "Compare Assets":
    st.header("⚖️ Compare Assets")

    symbols_input = st.text_input("Enter symbols (comma-separated)", value="AAPL, GOOGL, MSFT")

    # Trading mode selection
    mode = st.radio("Chart Mode", ["Day Trading", "Long Term"], horizontal=True, key="compare_mode")

    if mode == "Day Trading":
        col1, col2 = st.columns(2)
        with col1:
            interval = st.selectbox("Interval", ["1m", "5m", "15m", "30m", "1h"], index=1, key="compare_interval")
        with col2:
            period = st.selectbox("Period", ["1d", "5d", "7d"], index=0, key="compare_period_day")
    else:
        interval = "1d"
        period = st.selectbox("Period", ["1mo", "3mo", "6mo", "1y"], index=1, key="compare_period_long")

    normalize = st.checkbox("Normalize to % change", value=True)

    if st.button("Compare", type="primary"):
        symbols = [s.strip().upper() for s in symbols_input.split(",")]

        with st.spinner("Loading data..."):
            chart_data = pd.DataFrame()

            for symbol in symbols:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period=period, interval=interval)

                if not hist.empty:
                    if normalize:
                        chart_data[symbol] = (hist["Close"] / hist["Close"].iloc[0] - 1) * 100
                    else:
                        chart_data[symbol] = hist["Close"]

        if not chart_data.empty:
            st.line_chart(chart_data)

            if normalize:
                st.caption("Chart shows percentage change from start of period")
        else:
            st.error("Could not load data for the given symbols")


# =============================================================================
# Page: Portfolio Tracker
# =============================================================================
elif page == "Portfolio Tracker":
    st.header("💼 Portfolio Tracker")

    st.markdown("Enter your holdings below:")

    # Default holdings
    if "holdings" not in st.session_state:
        st.session_state.holdings = [
            {"symbol": "AAPL", "quantity": 10},
            {"symbol": "MSFT", "quantity": 5},
            {"symbol": "BTC-USD", "quantity": 0.5},
        ]

    # Editable holdings
    edited_holdings = st.data_editor(
        st.session_state.holdings,
        num_rows="dynamic",
        column_config={
            "symbol": st.column_config.TextColumn("Symbol", help="e.g., AAPL, BTC-USD"),
            "quantity": st.column_config.NumberColumn("Quantity", min_value=0, format="%.4f"),
        },
        use_container_width=True
    )

    if st.button("Calculate Portfolio Value", type="primary"):
        with st.spinner("Fetching prices..."):
            portfolio_data = []
            total_value = 0

            for holding in edited_holdings:
                if holding["symbol"] and holding["quantity"]:
                    data = get_price(holding["symbol"])
                    if data and data["price"]:
                        value = data["price"] * holding["quantity"]
                        total_value += value
                        portfolio_data.append({
                            "Symbol": data["symbol"],
                            "Name": data["name"],
                            "Quantity": holding["quantity"],
                            "Price": f"${data['price']:,.2f}",
                            "Value": f"${value:,.2f}",
                        })

        if portfolio_data:
            st.dataframe(pd.DataFrame(portfolio_data), use_container_width=True, hide_index=True)
            st.success(f"**Total Portfolio Value: ${total_value:,.2f}**")
        else:
            st.warning("No valid holdings to calculate")


# =============================================================================
# Page: Price Alerts
# =============================================================================
elif page == "Price Alerts":
    st.header("🔔 Price Alerts")

    st.markdown("Check if any assets have crossed your target prices:")

    # Default alerts
    if "alerts" not in st.session_state:
        st.session_state.alerts = [
            {"symbol": "AAPL", "target": 200, "direction": "above"},
            {"symbol": "BTC-USD", "target": 100000, "direction": "above"},
            {"symbol": "TSLA", "target": 300, "direction": "below"},
        ]

    edited_alerts = st.data_editor(
        st.session_state.alerts,
        num_rows="dynamic",
        column_config={
            "symbol": st.column_config.TextColumn("Symbol"),
            "target": st.column_config.NumberColumn("Target Price", min_value=0, format="$%.2f"),
            "direction": st.column_config.SelectboxColumn("Alert When", options=["above", "below"]),
        },
        use_container_width=True
    )

    if st.button("Check Alerts", type="primary"):
        with st.spinner("Checking prices..."):
            results = []

            for alert in edited_alerts:
                if alert["symbol"] and alert["target"]:
                    data = get_price(alert["symbol"])
                    if data and data["price"]:
                        is_triggered = (
                            (alert["direction"] == "above" and data["price"] >= alert["target"]) or
                            (alert["direction"] == "below" and data["price"] <= alert["target"])
                        )
                        results.append({
                            "Symbol": data["symbol"],
                            "Current Price": f"${data['price']:,.2f}",
                            "Target": f"${alert['target']:,.2f}",
                            "Condition": f"Price {alert['direction']} target",
                            "Status": "🚨 TRIGGERED" if is_triggered else "⏳ Waiting",
                        })

        if results:
            st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)

            triggered_count = sum(1 for r in results if "TRIGGERED" in r["Status"])
            if triggered_count > 0:
                st.warning(f"{triggered_count} alert(s) triggered!")
            else:
                st.info("No alerts triggered yet")


# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Built with [yfinance](https://github.com/ranaroussi/yfinance) & [Streamlit](https://streamlit.io)")
