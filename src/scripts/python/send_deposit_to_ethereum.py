from web3 import Web3

def send_deposit_to_ethereum(private_key, to_address, amount):
    # Connect to the Ethereum network using Infura or a local node
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

    # Prepare the transaction details
    account = w3.eth.account.privateKeyToAccount(private_key)
    nonce = w3.eth.getTransactionCount(account.address)
    gas_price = w3.eth.gas_price
    gas_limit = 21000  # Standard gas limit for Ethereum transactions

    transaction = {
        'nonce': nonce,
        'to': to_address,
        'value': w3.toWei(amount, 'ether'),
        'gas': gas_limit,
        'gasPrice': gas_price,
    }

    # Sign the transaction with the account's private key
    signed_txn = w3.eth.account.signTransaction(transaction, private_key)

    try:
        # Send the signed transaction to the Ethereum network
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

        if txn_receipt.status == 1:
            print("Deposit successfully sent to Ethereum address.")
        else:
            print("Failed to send deposit to Ethereum address.")

    except Exception as e:
        print("Error occurred while sending deposit to Ethereum address:", str(e))

# Example usage:
private_key = "0xABCDEF..."  # Replace with the actual private key
to_address = "0x123456..."  # Replace with the recipient's Ethereum address
amount = 0.5  # Specify the amount to be sent in Ether
send_deposit_to_ethereum(private_key, to_address, amount)
