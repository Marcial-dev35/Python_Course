# 1. Funtion definition
def process_batch(machine, ok_pieces, rejected_pieces):
    # 2. Calculated variables
    total = ok_pieces + rejected_pieces
    efficiency = (ok_pieces / total) * 100
    # 3. Return values
    return total, efficiency
#4. Try and exception handling
try:
    print("--- Industrial Data Entry ---")
    machine = input("Enter machine name:")
    ok = int(input("Enter OK pieces:"))
    rejected = int(input("Enter rejected pieces:"))

    #5. Function call and unpacking
    total_prod, eff_rate = process_batch(machine, ok, rejected)

    #6. Output results and save to file
    report_text = f"Machine: {machine} | Total: {total_prod} | Efficiency: {eff_rate: .2f}%"
    print(f"\n Success: {report_text}")

    with open("daily_report.txt", "a") as file:
        file.write(report_text + "\n")
        print("Data saved to daily_report.txt")

except ValueError:
    print("Eroor: Please enter numeric values for the pieces!")

except ZeroDivisionError:
    print("Error: Total pieces cannot be zero!")
    
    
