# === bank_account.py ===
class BankAccount:
"""A simple BankAccount class demonstrating encapsulation and basic operations."""


def __init__(self, initial_balance: float = 0.0):
self._account_balance = float(initial_balance)


def deposit(self, amount: float) -> None:
if amount < 0:
raise ValueError("Deposit amount must be non-negative")
self._account_balance += float(amount)


def withdraw(self, amount: float) -> bool:
if amount < 0:
raise ValueError("Withdraw amount must be non-negative")
if amount <= self._account_balance:
self._account_balance -= float(amount)
return True
return False


def display_balance(self) -> None:
print(f"Current Balance: ${self._account_balance:.2f}")




# === main-0.py (command-line interface for BankAccount) ===
import sys
from bank_account import BankAccount




def main():
account = BankAccount(100) # Example starting balance
if len(sys.argv) < 2:
print("Usage: python main-0.py <command>:<amount>")
print("Commands: deposit, withdraw, display")
sys.exit(1)


command, *params = sys.argv[1].split(':')
amount = float(params[0]) if params else None


if command == "deposit" and amount is not None:
account.deposit(amount)
print(f"Deposited: ${amount:.0f}" if amount.is_integer() else f"Deposited: ${amount}")
elif command == "withdraw" and amount is not None:
if account.withdraw(amount):
print(f"Withdrew: ${amount:.0f}" if amount.is_integer() else f"Withdrew: ${amount}")
else:
print("Insufficient funds.")
elif command == "display":
account.display_balance()
else:
print("Invalid command.")




if __name__ == "__main__":
main()

