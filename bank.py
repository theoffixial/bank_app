class AccHolder():
    def __init__(self, account_number, name, bank_name):
        self.account_number = account_number
        self.name = name
        self.bank_name = bank_name
        self.current_balance = 0

    def deposit(self, amount):
        self.current_balance += amount
        return self.current_balance

    def withdrawal(self, amount):
        if self.current_balance - amount < 0:
            return f"You can't withdraw more than your current balance ({self.current_balance})"
        self.current_balance -= amount
        return self.current_balance



# I Created a dictionary to store account owners, this will be our database in real time
account_owners = {
    "1234567890": {"name": "Alice", "bank_name": "Bank A"},
    "9876543210": {"name": "Bob", "bank_name": "Bank B"},
}

# This is a function to display account informations
def display_account_info(account_number):
    owner_info = account_owners.get(account_number)
    if owner_info:
        account_holder = AccHolder(account_number, owner_info["name"], owner_info["bank_name"])
        return account_holder
    else:
        return None
