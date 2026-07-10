# Defining a function
# def welcome():
#     print("Hello world")
# welcome()

# Passing values 
# def add(a,b):
#     total = (a+b)
#     print("The sum is: " ,total)

# add(10,20)
# x = 30
# y = 20
# add(x,y)

# Even & Odd program
def evenOdd(number):
    if number % 2 == 0:
        return "Even" 
    else:
        return "Odd" 
    
result = evenOdd(2)
print("The result is: ", result)

# Compact version using ternary operator
def evenOdd(numbers):
    return "Even" if numbers % 2 == 0 else "Odd"

result = int(input("Enter a number: "))
print("The number is: ", evenOdd(result))
