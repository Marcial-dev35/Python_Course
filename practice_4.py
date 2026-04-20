def check_temperature(sensor_id, current_temp, max_temp = 85.0):
    margin = max_temp - current_temp
    return sensor_id, margin

try:
    id = str(input("Enter the ID sensor: "))
    temp = float(input("Enter the current temperature: "))

    sensor_id, temp_margin = check_temperature(id, temp)
    print(f"Sensor ID: {sensor_id} | Temperature Margin: {temp_margin:.2f}°C")

    with open("thermal_log.txt", "a") as file:
        file.write(f"Sensor ID: {sensor_id} | Temperature Margin: {temp_margin:.2f}°C\n")

except ValueError:
    print("Error: Please enter a valid number for the temperature!")
    