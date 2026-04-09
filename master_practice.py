# Dictionary to store the settings for the master practice
settings = {
    "min_measure": 50.0,
    "max_measure": 150.0
}
# Empty list to store the practice results
production_log = []
print("--- Steel Production System Started ---")

# Main Loop
while True:
    entry = input("Enter piece measure (or 'exit' to finish)")
    if entry.lower() == "exit":
        break
    try:

    # Logic to check the measure and store the result
        measure = float(entry)
        if settings["min_measure"] <= measure <= settings["max_measure"]:
            production_log.append((measure, "APPROVED"))
        else:
            print("Piece rejected: measure out of range.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print("--- Steel Production System Ended ---")
# Final Storage (Saving thr list to a file)
if len(production_log) > 0:
    with open("shift_summary.txt", "a") as file:
        file.write("--- NEW PRODUCTION BATCH ---\n")
        for item in production_log:
            file.write(f"Approved Measure: {item}\n")
        file.write("-----------------------------------\n\n")
    print(f"Success! {len(production_log)} items saved to shift_summary.txt")
else:
    print("No items to save today.")
print("System offline. Have a great shift at the factory, Marcial!")

