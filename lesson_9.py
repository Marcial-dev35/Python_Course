def verificar_pieza(medida):
    if medida > 45 < 55:
        return "APROBADA"
    else:
        return "RECHAZADA"
    
medida = float(input("Cual es la medida de la pieza actual?: "))
estado = verificar_pieza(medida)
print(f"Marcial, la pieza ha sido {estado}")
