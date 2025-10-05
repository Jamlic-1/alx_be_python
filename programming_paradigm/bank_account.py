class BankAccount:
    def __init__(self, initial_balance=0.0):
        # store as float for correct formatting and arithmetic
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        # accept numeric input (caller should pass a valid number)
        self.__account_balance += float(amount)

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self):
        # accessor in case tests want to inspect the numeric value
        return self.__account_balance

    def display_balance(self):
        # improved formatting: always show two decimals and thousands separators
        print(f"Current Balance: ${self.__account_balance:,.2f}")
