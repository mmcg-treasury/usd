import requests

def check_zelle_account_balance(email):
    # Prepare API request payload
    payload = {
        "email": email
    }

    try:
        # Send API request to check the balance of the Zelle account
        response = requests.post("https://api.example.com/check_zelle_account_balance", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        account_balance = response.json().get("account_balance")
        if account_balance:
            print("Zelle account balance:", account_balance)
        else:
            print("Failed to retrieve Zelle account balance.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while checking Zelle account balance:", str(e))

# Example usage:
check_zelle_account_balance("jane@example.com")
