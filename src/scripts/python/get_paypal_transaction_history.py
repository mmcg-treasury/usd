import requests

def get_paypal_transaction_history(email):
    # Prepare API request payload
    payload = {
        "email": email
    }

    try:
        # Send API request to retrieve the transaction history from PayPal
        response = requests.post("https://api.example.com/get_paypal_transaction_history", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        transaction_history = response.json().get("transaction_history")
        if transaction_history:
            for transaction in transaction_history:
                print("Transaction ID:", transaction["transaction_id"])
                print("Amount:", transaction["amount"])
                print("Description:", transaction["description"])
                print("---")

        else:
            print("No transaction history found for the PayPal account.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while retrieving PayPal transaction history:", str(e))

# Example usage:
get_paypal_transaction_history("john@example.com")
