# Taking input from user and print it.

Name = input("Enter your name here: ")            #Asking Name from user as a string.
Age = input("Enter your age here: ")               #Asking for age from user as a integer.                                  
Height = float(input("Enter your height here: ")) #Asking Height from the user as a float.

# Print them.
print("Your name is :" ,Name)
print("Your age is: " ,Age)
print("Your height is: " ,Height)

#taking input of same data type in one line by using map() function and input.split() method.

a , b, c = map(int, input("Enter: ").split())

print( a,b,c)