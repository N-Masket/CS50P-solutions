import sys
import requests

def get_bitcoin_price():
    try:
        url = "https://rest.coincap.io/v3/assets/bitcoin"
        headers = {
            "Authorization": "Bearer 451641e7373c8d1a70f552f33927ebeffb3f9e4a382534b3889b59f9e2fcc77e"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        # Convert string price to float
        bitcoin_price = float(data['data']['priceUsd'])
        
        if len(sys.argv) == 1:
                print("Missing command line arguments")
                raise ValueError
        else:
            try:
                print("sys.argv:", sys.argv)
                n = float(sys.argv[1])  # Convert user input to float
                usd_price = n * bitcoin_price
                print(f"${usd_price:,.4f}")
            except TypeError:
                print("Command-line argument is not a number")

    except requests.RequestException:
        print("Error connecting to the API")

get_bitcoin_price()
