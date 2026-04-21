# 1. Dictionary creation
operario_actual = {
    "nombre": "Marcial",
    "sector": "Forja",
    "piezas_objetivo": 250
}
print(f"El operario {operario_actual['nombre']} debe producir {operario_actual['piezas_objetivo']} piezas hoy.")
# 2. Modifying dictionary values
operario_actual["piezas_objetivo"] = 300
operario_actual["equipo_seguridad"] = "Completo"
del operario_actual["sector"]
# 3. Displaying the updated dictionary
print(operario_actual)