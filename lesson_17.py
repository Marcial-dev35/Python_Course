# --- The Plant's Main Database ---
factory_database = {
    "night_shift": {
        "supervisor": "Marcial",
        "machines": {
            "lathe_01": {
                "status": "maintenance", 
                "temp": 45
            },
            "oven_05": {
                "status": "active", 
                "temp": 850
            }
        }
    }
}

# --- YOUR TASKS START HERE ---

# Task 1 (Read): Print the temperature of 'oven_05'. 
# Hint: You will need FOUR sets of brackets! [][][][]

# Task 2 (Update): The maintenance is done. Change the 'status' of 'lathe_01' to "active".

# Task 3 (Create): A new machine arrived. Add "press_02" inside the "machines" dictionary.
# It needs its own dictionary with "status": "standby" and "temp": 20.

# Task 4 (Delete): The 'lathe_01' doesn't need a temperature sensor anymore. Delete the "temp" key from 'lathe_01'.

# Final Report: Print the entire factory_database to verify.
print(f"TThe temperature of oven is: {factory_database['night_shift']['machines']['oven_05']['temp']}")
factory_database["night_shift"]["machines"]["lathe_01"]["status"] = "active"
factory_database["night_shift"]["machines"]["press_02"] = {"status": "standby", "temp": 20}
del factory_database["night_shift"]["machines"]["lathe_01"]["temp"]
print(factory_database)