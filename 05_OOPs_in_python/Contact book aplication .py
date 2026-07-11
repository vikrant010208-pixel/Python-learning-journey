class BankAccount:
    """A class representing a simple bank account."""

    def __init__(self, owner_name, initial_balance=0):
        self.owner = owner_name
        self.__balance = max(0, initial_balance)  # Prevent negative balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f" Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print(" Withdrawal amount must be greater than 0.")
        elif amount > self.__balance:
            print(" Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.__balance}")

    def get_balance(self):
        """Return the current account balance."""
        return self.__balance


# ------------------ Main Program ------------------

# Create objects
account_a = BankAccount("Amit Sharma", 5000)
account_b = BankAccount("Priya Patel", 12000)

# Account A operations
print(f"--- {account_a.owner}'s Account ---")
account_a.deposit(1500)
account_a.withdraw(2000)
print(f"Current Balance: ₹{account_a.get_balance()}")

# Account B operations
print(f"\n--- {account_b.owner}'s Account ---")
account_b.withdraw(15000)   # Insufficient balance
account_b.deposit(3000)
print(f"Current Balance: ₹{account_b.get_balance()}")