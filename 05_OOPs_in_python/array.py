import array

numbers = array.array('i', [10, 20, 30, 40, 50])

print(numbers[2])  # Accessing Element by index

# Accessing the whole array using for loop
for i in numbers:
    print(i)

# Add some thing in array
numbers.append(60)
print(numbers)

# Remove a specific element
numbers.remove(10)
print(numbers)

# Reverse an array
numbers.reverse
print(numbers)