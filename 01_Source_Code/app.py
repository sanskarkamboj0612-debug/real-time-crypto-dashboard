import streamlit as st
import requests
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Real-Time Crypto Dashboard",
    page_icon="📈",
    layout="wide"
)

# Auto Refresh Every 30 Seconds
st_autorefresh(interval=30000, key="refresh")

# ---------------------------------------------------
# Dashboard Title
# ---------------------------------------------------

st.title("📈 Real-Time Crypto Dashboard")
st.markdown("### Live Cryptocurrency Prices using CoinGecko API")

st.markdown("---")

# ---------------------------------------------------
# Cryptocurrency Selection
# ---------------------------------------------------

coins = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Solana": "solana"
}

selected_coin = st.selectbox(
    "Select Cryptocurrency",
    list(coins.keys())
)

coin_id = coins[selected_coin]

# ---------------------------------------------------
# CoinGecko API
# ---------------------------------------------------

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": coin_id,
    "vs_currencies": "usd"
}

try:

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    price = data[coin_id]["usd"]

    last_updated = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # ---------------------------------------------------
    # Dashboard Metrics
    # ---------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label=f"{selected_coin} Price (USD)",
            value=f"${price:,}"
        )

    with col2:
        st.metric(
            label="Last Updated",
            value=last_updated
        )

    st.markdown("---")

    # ---------------------------------------------------
    # Price Alert
    # ---------------------------------------------------

    st.subheader("🔔 Price Alert")

    threshold = st.number_input(
        "Enter Alert Price (USD)",
        min_value=0,
        value=50000,
        step=1000
    )

    if price >= threshold:

        st.success(
            f"✅ Alert: {selected_coin} price is above ${threshold:,}"
        )

    else:

        st.warning(
            f"⚠ Current {selected_coin} price is below ${threshold:,}"
        )

except requests.exceptions.RequestException:

    st.error(
        "❌ Unable to fetch live data from CoinGecko API. Please try again later."
    )