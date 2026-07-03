# Taking input form th users.
marks = int(input("Enter your marks here to check: "))

# Condition to check
if marks <33:
    print("F garde")
elif marks <=45:
    print("E grade")
elif marks <=65:
    print("D grade")
elif marks <=75:
    print("C grade")
elif marks <=85:
    print("B grade")
elif marks <=100:
    print("A grade")
else:
    print("Invalid marks! Please Enter again.")