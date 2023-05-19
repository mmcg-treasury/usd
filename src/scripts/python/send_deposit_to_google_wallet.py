import requests

def send_deposit_to_google_wallet(name, email, amount, description):
    # Prepare API request payload
    payload = {
        "name": name,
        "email": email,
        "amount": amount,
        "description": description
    }

    try:
        # Send API request to send the deposit to Google Wallet
        response = requests.post("https://api.example.com/send_deposit_to_google_wallet", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        if response.json().get("status") == "success":
            print("Deposit successfully sent to Google Wallet.")
        else:
            print("Failed to send deposit to Google Wallet.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while sending deposit to Google Wallet:", str(e))

# Example usage:
send_deposit_to_google_wallet("Jane Smith", "jane@example.com", 75.0, "Payment for services")
