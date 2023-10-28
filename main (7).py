class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. Current balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. Current balance: ${self.__account_balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account Number: {self.__account_number}\nAccount Holder: {self.__account_holder_name}\nCurrent Balance: ${self.__account_balance}"


# Test the BankAccount class
account = BankAccount("123456789", "John Doe", 1000)
print(account.deposit(500))  # Deposited $500. Current balance: $1500
print(account.withdraw(200))  # Withdrew $200. Current balance: $1300
print(account.display_balance())