# API Data Transformer

A Python script that fetches live cryptocurrency data from CoinGecko API, cleans it, and exports the results to JSON.

## What it does
- Fetches real-time coin data from the CoinGecko public API
- Filters out coins under $1000usd
- Transforms raw API response into clean dictionaries
- Sorts by price (highest to lowest)
- Exports cleaned data to 'cleaned_coins.json'

## Tech used
- Python 3
- 'requests'
- CoinGecko public API (no key required)

## How to run
```bash
git clone https://github.com/anthfish/api-data-transformer.git
cd api-data-transformer
python3 -m venv venv
source venv/bin/activate
pip install requests
python3 coin_cleaner.py
```

## Output
Prints filtered coins to the terminal and saves a 'cleaned_coins.json' file in the project directory.
