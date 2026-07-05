n = int(input("Enter a number: "))
counter = 0
if n == 0:
    counter+=1
while n>0:
    counter += 1
    n = n//10
print(counter)

