# 1. Variable
operator_name = input("Please enter the operator's name: ")
pieces_count = int(input("Please enter the number of pieces produced: "))

# 2. Conditional statement
if pieces_count > 100:
    status = "HIGH"
else:
    status = "STANDARD"

# 3. Storage in a file
with open("production_report.txt", "a") as file:
    file.write(f"Operator: {operator_name}, Production Status: {status}, Pieces Produced: {pieces_count}\n")