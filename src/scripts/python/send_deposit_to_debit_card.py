import requests

def send_deposit_to_debit_card(name, debit_card_number, amount, description):
    # Prepare API request payload
    payload = {
        "name": name,
        "debit_card_number": debit_card_number,
        "amount": amount,
        "description": description
    }

    try:
        # Send API request to send the deposit to the debit card
        response = requests.post("https://api.example.com/send_deposit_to_debit_card", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        if response.json().get("status") == "success":
            print("Deposit successfully sent to debit card.")
        else:
            print("Failed to send deposit to debit card.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while sending deposit to debit card:", str(e))

# Example usage:
send_deposit_to_debit_card("John Doe", "1234567890123456", 150.0, "Refund")
