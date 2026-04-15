try:
    age = int(input("Enter you age:"))
    print(f"Nice, age of {age} recorded.")
except ValueError:
    print("Invalid age! Use numbers only.")