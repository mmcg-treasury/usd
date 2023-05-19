import requests

def generate_wallet_address(user_id):
    # Prepare API request payload
    payload = {
        "user_id": user_id
    }

    try:
        # Send API request to generate a unique wallet address for the user
        response = requests.post("https://api.example.com/generate_wallet_address", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        wallet_address = response.json().get("wallet_address")
        if wallet_address:
            print(f"A unique wallet address {wallet_address} is generated for user {user_id}.")
        else:
            print("Failed to generate a wallet address for the user.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while generating a wallet address:", str(e))

# Example usage:
user_id = "12345"
generate_wallet_address(user_id)
