# 1. Variables en ingles
steel_stock = [50.5, 100.0, 150.2]


# 2. Definicion de funcion en ingles
def is_valid(measure):
    if measure > 0:
        return True
    else:
        return False
    
# 3. Entrada de datos
measure_input = float(input("Please enter the measure of the piece: "))

# 4. Llamando a la funcion y revisando el resultado
if is_valid(measure_input):
    steel_stock.append(measure_input)
    print(f"Success! The update stock is: {steel_stock}")
else:
    print("ERROR: Invalid measure. Must be greater than zero.")
