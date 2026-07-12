import requests
from datetime import datetime

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin",
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)

data = response.json()

# Extract Data
bitcoin_price = data["bitcoin"]["usd"]

current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

print("Coin        :", "Bitcoin")
print("Price (USD) :", bitcoin_price)
print("Updated At  :", current_time)



import pandas as pd

crypto_df = pd.DataFrame({
    "Coin": ["Bitcoin"],
    "Price (USD)": [bitcoin_price],
    "Last Updated": [current_time]
})

print(crypto_df)