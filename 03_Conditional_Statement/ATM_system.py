print("=== WELCOME TO DIGITAL ATM ====")

balance = 10000
pin = 1234

while True:

    entered_pin = int(input("Enter your pin: "))

    if entered_pin == pin:

        print("======= MENU ======")

        print("1. Check balance.")
        print("2. Withdraw Money.")
        print("3. Deposit Money.")
        print("4. Exit.")

        choice = input("\nSelect An Option (1, 2, 3, 4): ")

        if choice == "1":

            print(f"Your current balance is ₹{balance}.")

        elif choice == "2":

            withdrawn = int(input("Enter Amount To Withdraw: "))
            
            if withdrawn > balance:
                print("Insufficient Balance! Please Enter Again.")

            elif withdrawn <= 0:
                print("Please enter a valid amount.")

            else:
                balance = balance - withdrawn

                print(withdrawn, "Withdrawn Successfully!")
                print("Your remaining balance is:", balance)

        elif choice == "3":

            deposit = int(input("Enter Amount To Deposit: "))

            if deposit <= 0:
                print("Please enter a valid amount.")

            else:
                balance = balance + deposit

                print(deposit, "Deposited Successfully!")
                print("Your current balance is: ₹", balance)

        elif choice == "4":

            print("Thank you for using ATM. 😊")
            break

        else:
            print("Invalid choice! Please select a valid option.")

    else:

        print("Incorrect PIN!")
