peso_total = int(input("Peso total de unas lamina de acero: "))
peso_piezas = float(input("Peso de las piezas obtenidas: "))
desperdicio = peso_total - peso_piezas
eficiencia = (peso_piezas / peso_total) * 100
print(f"Marcial, el desperdicio es de {desperdicio} kg y la eficiencia es del {eficiencia} %.")