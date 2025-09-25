# -------------------------------------------
# Exercise: Learn about variables in Python
# -------------------------------------------
# This program currently repeats itself and hard-codes data.
# Your task: Use variables to make the code shorter and easier to change!

# Step 1: Run this program as it is first:
name = "Alice"
age = 25
favefood = "pizza"

print(f"Hello, {name}!")
print(f"{name} is {age} years old.")
print(f"In 5 years, {name} will be {age + 5} years old.")
print(f"{name} really likes pizza.")
print(f"Pizza is {name}'s favourite food!")

# This will just add an empty line for space
# Please don't touch this
print("")

second_name = "Bob Hope"
second_age = 100
second_favefood = "Lemon pie"

print(f"Hello, {second_name}!")
print(f"{second_name} is {second_age} years old.")
print(f"In 5 years, {second_name} will be {second_age + 5} years old.")
print(f"{second_name} really likes {second_favefood}.")
print(f"{second_favefood} is {second_name}'s favourite food!")

print("")

Third_name = "Bob Ross"
Third_age = 52
Third_favefood = "Hamburgers"

print(f"Hello, {second_name}!")
print(f"{second_name} is {second_age} years old.")
print(f"In 5 years, {second_name} will be {second_age + 5} years old.")
print(f"{second_name} really likes {second_favefood}.")
print(f"{second_favefood} are {second_name}'s favourite food!")

print("")

fourth_name = ""
fourth_age = ""
fourth_favefood = ""

fourth_name = input("What about you, what is your name? ")
fourth_age = int(input("And your age? "))
fourth_favefood = input("And now your favourite food? ")

print("")

print(f"Hello, {fourth_name}!")
print(f"{fourth_name} is {fourth_age} years old.")
print(f"In 5 years, {fourth_name} will be {fourth_age + 5} years old.")
print(f"{fourth_name} really likes {fourth_favefood}.")
print(f"{fourth_favefood} is {fourth_name}'s favourite food!")
# Notice there's lots of repetition!
# If we want to change Alice's age or favourite food, we'd have to change it in many places.

# Step 2: Refactor using variables:
# 1. Create variables for name, age, and favourite food.
# 2. Replace the hard-coded text with variables using f-strings.
# Example:
# name = "Alice"
# age = 25
# food = "pizza"
# print(f"Hello, {name}!")
# print(f"{name} is {age} years old.")
# print(f"In 5 years, {name} will be {age + 5} years old.")
# print(f"{name} really likes {food}.")
# print(f"{food.capitalize()} is {name}'s favourite food!")

# Step 3: Do the same for Bob, or make your own second person!
# Use different values for name, age, and food.

# Step 4: Add a third person with their own data.
# This should now be much quicker since you only need to change variables,
# not rewrite all the print statements.

# -------------------------------------------
# 💡 Extra Challenge (optional):
# - Use input() to ask the user for their name, age, and favourite food.
# - Then print a message using what they typed in!
# Example:
# name = input("What is your name? ")
# age = int(input("How old are you? "))
# food = input("What is your favourite food? ")
# print(f"Hello, {name}! Next year you will be {age + 1}.")
# print(f"{food.capitalize()} is your favourite food!")

# Once you are done, please run the following commands (one by one) in the terminal:
# git add Ex1_variables.py
# git commit -m "Completed variables exericse"
# git push origin main