# Random User_name generator
import random

name = input("Enter your name: ").lower()
number = random.randint(10,90)

styles = [
    name + str(number),
    name + "_dev" + str(number),
    "its_" + name,
    name + "_x"
]

print("\n💖 USERNAME GENERATOR")

for i, username in enumerate(styles, 1):
    print(f"{i}.@{username}")