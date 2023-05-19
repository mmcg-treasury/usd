import requests

def send_deposit_to_checking(name, address, phone_number, email, account_number, routing_number, amount, description):
    # Prepare API request payload
    payload = {
        "name": name,
        "address": address,
        "phone_number": phone_number,
        "email": email,
        "account_number": account_number,
        "routing_number": routing_number,
        "amount": amount,
        "description": description
    }

    try:
        # Send API request to send the deposit to the checking account
        response = requests.post("https://api.example.com/send_deposit_to_checking", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        if response.json().get("status") == "success":
            print("Deposit successfully sent to checking account.")
        else:
            print("Failed to send deposit to checking account.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while sending deposit to checking account:", str(e))

# Example usage:
send_deposit_to_checking("Jane Smith", "456 Elm St", "555-987-6543", "jane@example.com",
                         "987654321", "123456789", 1000.0, "Payment for services")
