import requests

def send_wire_transfer_with_compliance(name, address, phone_number, email, account_number, routing_number, amount, description):
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
        # Perform compliance checks before initiating the wire transfer
        compliance_check_response = requests.post("https://api.example.com/compliance/check", json=payload)
        compliance_check_response.raise_for_status()  # Raise an exception for non-2xx responses

        if compliance_check_response.json().get("status") != "approved":
            print("Wire transfer cannot be processed due to compliance issues.")
            return

        # Send API request to initiate the wire transfer
        response = requests.post("https://api.example.com/send_wire_transfer", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        if response.json().get("status") == "success":
            print("Wire transfer initiated successfully.")
        else:
            print("Failed to initiate wire transfer.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while sending wire transfer:", str(e))

# Example usage:
send_wire_transfer_with_compliance("John Doe", "123 Main St", "555-123-4567", "john@example.com",
                                   "123456789", "987654321", 5000.0, "Business transaction")
