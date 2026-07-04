"""Problem 3: List FilterGiven a list of mixed data types [10, "apple", 25, "banana", 3.14, 50],use a loop to create a new list
containing only the integers greater than 15."""

# Code here
mixed_list = [10, "apple", 25, "banana", 3.14, 50]
filtered_list = []

for item in mixed_list:
    if type(item) == int:
        filtered_list.append(item)

print("This is the filtered list = " ,filtered_list)