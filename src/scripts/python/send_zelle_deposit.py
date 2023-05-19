import requests

def send_deposit_to_zelle(name, email, amount, description):
    # Prepare API request payload
    payload = {
        "name": name,
        "email": email,
        "amount": amount,
        "description": description
    }

    # Send API request to send the deposit to Zelle
    response = requests.post("https://api.example.com/send_zelle_deposit", json=payload)

    # Handle the response and perform necessary error checking and logging

# Example usage:
send_deposit_to_zelle("John Doe", "john@example.com", 200.0, "Reimbursement")
