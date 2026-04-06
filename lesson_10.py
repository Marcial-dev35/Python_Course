pieza = input("Cual es el nombre de la pieza?: ")
estado = input("Marcial, cual es el estado de la pieza? (APROBADA/RECHAZADA): ")
with open("reporte_diario.txt", "a") as archivo:
    archivo.write(f"Pieza: {pieza}, Estado: {estado}\n")