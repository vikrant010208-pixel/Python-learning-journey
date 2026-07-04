print("=== WELCOME TO DIGITAL ATM ====")

balance = 10000
pin = 1234

entered_pin = int(input("Enter your pin: "))

if entered_pin == pin:
    print("======= MENU ======")
    print("1. Check balance.")
    print("2. Withdraw Money.")
    print("3. Deposit Money.")
    print("4. Exit.")

choice = input("\n Select An Option (1 , 2 , 3 , 4): ")

if choice == "1":
    print(f"Your current balance is ₹{balance}.")

elif choice == "2":
    withdrawn = int(input("Enter Amount To Withdraw: "))

if withdrawn > 10000:
    print("Insufficient Amount! Please Enter Again.")

elif withdrawn <= 10000:
    balance = balance - withdrawn
    print(withdrawn, "Withdrawn Successfully!")
    print("Your remaining balance is: " ,balance)

elif choice == "3":
    deposit = int(input("Enter Amount To Deposit: "))
    balance = balance + deposit
    print(deposit, "Deposited Successfully!")
    print("Your current balance is: ₹" ,balance)

elif choice == "4":
    print("Thankyou for using ATM.")
