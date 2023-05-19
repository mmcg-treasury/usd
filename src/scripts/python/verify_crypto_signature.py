import hashlib
import requests

def verify_crypto_signature(transaction_id, signature):
    # Prepare API request payload
    payload = {
        "transaction_id": transaction_id,
        "signature": signature
    }

    tr:
        # Send API request to verify the authenticity of the digital signature
        response = requests.post("https://api.example.com/verify_crypto_signature", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses

        # Handle the response and perform necessary error checking and logging
        if response.json().get("is_authentic"):
            print("The digital signature is authentic.")
        else:
            print("The digital signature is not authentic.")

    except requests.exceptions.RequestException as e:
        print("Error occurred while verifying the digital signature:", str(e))

# Example usage:
transaction_id = "123456789"
signature = "0xABCDEF..."
verify_crypto_signature(transaction_id, signature)
