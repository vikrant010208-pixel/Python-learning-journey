# Create three variable Name , course , semester , and enter the details and print a sentence.

Name = "Vikrant kumar"
Course = "BCA course"
Semester = "3rd"

print(f"My name is " + str(Name) , "I am pursuing " + str(Course), "in semester " + str(Semester))

# You are given the following two variables. Notice that one is a string and the other is an integer:
# birth_year = "2008"
# current_age = 18
# Write the Python code to convert birth_year into a usable integer. Then, add it to current_age and print the resulting current year.

birth_year = "2008"
current_age = 18

Current_year = int(birth_year) + current_age

print(Current_year)