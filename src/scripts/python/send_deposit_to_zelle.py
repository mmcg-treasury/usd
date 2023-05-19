import requests

def send_deposit_to_zelle(name, email, amount, description):
    # Prepare API request payload
    payload = {
        "name": name,
        "email": email,
        "amount": amount,
        "description": description
    }

    try:
        # Send API request to send the deposit to Zelle
        response = requests.post("https://api.example.com/send_deposit_to_zelle", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        if response.json().get("status") == "success":
            print("Deposit successfully sent to Zelle.")
        else:
            print("Failed to send deposit to Zelle.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while sending deposit to Zelle:", str(e))

# Example usage:
send_deposit_to_zelle("Jane Smith", "jane@example.com", 150.0, "Payment for services")
