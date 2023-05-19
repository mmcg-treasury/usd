def collect_deposit_information(deposit_type):
    name = input("Recipient's Name: ")
    address = input("Recipient's Address: ")
    phone_number = input("Recipient's Phone Number: ")
    email = input("Recipient's Email Address: ")
    amount = float(input("Amount to be sent: "))
    description = input("Description of Payment: ")

    # Additional code to validate and process the collected information

# Example usage:
collect_deposit_information("checking")
