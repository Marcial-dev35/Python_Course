cantidad_lote = int(input("Cuantas piezas se van a fabricar hoy?: "))
if cantidad_lote < 0:
    print("ERROR: La cantidad debe ser un numero positivo mayor a cero.")
else:
    for pieza in range(cantidad_lote):
        print(f"Pieza # {pieza + 1} fabricada con exito [OK]")
print("Piezas producidas con exito.Felicidades Marcial.")