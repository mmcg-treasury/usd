import requests

def check_crypto_market_price(coin):
    # Prepare API request payload
    payload = {
        "coin": coin
    }

    try:
        # Send API request to retrieve the current market price of the cryptocurrency
        response = requests.get("https://api.example.com/check_crypto_market_price", params=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        market_price = response.json().get("market_price")
        if market_price:
            print(f"The current market price of {coin} is {market_price}.")
        else:
            print("Failed to retrieve the market price for the cryptocurrency.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while checking cryptocurrency market price:", str(e))

# Example usage:
check_crypto_market_price("BTC")
