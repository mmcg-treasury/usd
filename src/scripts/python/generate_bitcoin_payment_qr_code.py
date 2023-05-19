import qrcode

def generate_bitcoin_payment_qr_code(address, amount):
    # Prepare the payment URL
    payment_url = f"bitcoin:{address}?amount={amount}"

    # Generate the QR code
    qr_code = qrcode.make(payment_url)

    # Save the QR code as an image file
    qr_code.save("bitcoin_payment_qr_code.png")

    print("Bitcoin payment QR code generated successfully.")

# Example usage:
generate_bitcoin_payment_qr_code("1ABCxyz...", 0.01)
