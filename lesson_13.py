
operator = "Marcial"
def star_shift():
    current_task = "Forging"
    return current_task
task_result = star_shift()
print(f"Operator name: {operator} - Task: {task_result}")

def calculate_pay(hours, rate=20.0):
    pay = hours * rate
    return pay
total_pay = calculate_pay(30)
print(f"Your pay is: ${total_pay}")
total_pay = calculate_pay(30, 25.0)
print(f"Your pay with extra is: ${total_pay}")
