import requests

def send_direct_deposit_to_business(name, address, phone_number, email, account_number, routing_number, amount, description):
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
        # Send API request to process the direct deposit to the business account
        response = requests.post("https://api.example.com/send_direct_deposit_to_business", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        if response.json().get("status") == "success":
            print("Direct deposit successfully sent to business account.")
        else:
            print("Failed to send direct deposit to business account.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while sending direct deposit to business account:", str(e))

# Example usage:
send_direct_deposit_to_business("John Doe", "123 Main St", "555-123-4567", "john@example.com",
                                "123456789", "987654321", 5000.0, "Invoice payment")
