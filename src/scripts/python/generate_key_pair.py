from Crypto.PublicKey import RSA

def generate_key_pair():
    # Generate a new RSA key pair
    key = RSA.generate(2048)

    # Extract the public and private keys
    public_key = key.publickey().export_key().decode()
    private_key = key.export_key().decode()

    # Save the keys securely in the user's account

    print("Public key:", public_key)
    print("Private key:", private_key)

# Example usage:
generate_key_pair()
