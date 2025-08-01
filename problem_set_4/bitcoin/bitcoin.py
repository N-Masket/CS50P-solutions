import sys
import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_bitcoin_price():
    try:
        url = "https://rest.coincap.io/v3/assets/bitcoin"
        token = os.getenv("COINCAP_API_KEY")  # Read from environment variable

        if not token:
            print("❗Error: COINCAP_API_KEY not set in your environment.")
            return

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        # Convert string price to float
        bitcoin_price = float(data['data']['priceUsd'])

        if len(sys.argv) == 1:
            print("Missing command line arguments")
            return
        else:
            try:
                n = float(sys.argv[1])  # Convert user input to float
                usd_price = n * bitcoin_price
                print(f"${usd_price:,.4f}")
            except ValueError:
                print("Command-line argument is not a valid number")

    except requests.RequestException:
        print("Error connecting to the API")

get_bitcoin_price()
