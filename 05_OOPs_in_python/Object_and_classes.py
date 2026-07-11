class BankAccount:
    """A class representing a simple bank account."""
    
    # 1. Constructor method to initialize the object
    def __init__(self, owner_name, initial_balance):
        self.owner = owner_name        # Instance variable (public)
        self.__balance = initial_balance  # Private variable (hidden from outside)

    # 2. A method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("❌ Invalid deposit amount!")

    # 3. A method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f" Withdrew ₹{amount}. Remaining balance: ₹{self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")

    # 4. A getter method to safely view the private balance
    def get_balance(self):
        return self.__balance


# --- EXECUTION (CREATING AND USING OBJECTS) ---

# Creating two unique objects (instances)
account_a = BankAccount("Amit Sharma", 5000)
account_b = BankAccount("Priya Patel", 12000)

# Interacting with Account A
print(f"--- {account_a.owner}'s Account ---")
account_a.deposit(1500)
account_a.withdraw(2000)

# Interacting with Account B
print(f"\n--- {account_b.owner}'s Account ---")
account_b.withdraw(15000)  # Will fail due to insufficient funds
print(f"Current Balance: ₹{account_b.get_balance()}")
