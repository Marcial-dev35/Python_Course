# This code demonstrates how to safely handle user input for age using a try-except block.
try:
    age = int(input("Enter you age:"))
    print(f"Nice, age of {age} recorded.")
except ValueError:
    print("Invalid age! Use numbers only.")