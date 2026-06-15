import requests
import json

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
response = requests.get(url)

if response.status_code == 200:
	raw_data = response.json()

	filtered = list(filter(lambda coin: coin["current_price"] > 1000, raw_data))

	def clean_coin(coin):
		return {
			"name": coin["name"],
			"symbol": coin["symbol"],
			"price": coin["current_price"]
		}
	cleaned = list(map(clean_coin, filtered))

	cleaned = sorted(cleaned, key=lambda coin: coin["price"], reverse=True)

	with open("cleaned_coins.json", "w") as f:
		json.dump(cleaned, f, indent=2)
	print("Saved to cleaned_coins.json")

	for coin in cleaned:
		print(f"{coin['name']} ({coin['symbol']}): ${coin['price']}")

else:
	print("Failed to fetch data.")

