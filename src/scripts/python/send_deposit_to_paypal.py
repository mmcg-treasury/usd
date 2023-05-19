import requests

def send_deposit_to_paypal(name, email, amount, description):
    # Prepare API request payload
    payload = {
        "name": name,
        "email": email,
        "amount": amount,
        "description": description
    }

    try:
        # Send API request to send the deposit to PayPal
        response = requests.post("https://api.example.com/send_deposit_to_paypal", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        if response.json().get("status") == "success":
            print("Deposit successfully sent to PayPal.")
        else:
            print("Failed to send deposit to PayPal.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while sending deposit to PayPal:", str(e))

# Example usage:
send_deposit_to_paypal("John Doe", "john@example.com", 200.0, "Payment for goods")
