print("===== WELCOME TO MINI CALCULATOR =====")

# Taking input 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Choosing an operator.
print("1. +")
print("2. -")
print("3. *")
print("4. /")
choice = input("\n Select an operator.")

# Perform an operation
if choice == "1":
    print("The addition of the two given number is: " ,num1 + num2)

elif choice == "2":
    print("The subtraction of the two given number is: " ,num1 - num2)

elif choice == "3":
    print("The multiplication of the given two number is: " , num1 * num2)

elif choice == "4":
    try:
        print("The division of the two given number is: " ,num1 / num2)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice! Please select a valid operator from the menu.")