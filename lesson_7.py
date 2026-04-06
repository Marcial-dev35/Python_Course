almacen = ["Viga", "Plancha", "Tubo"]
print(f"Segundo producto actual: {almacen[1]}")
nuevo = input("Agrega un  uevo producto a la lista: ")
almacen.append(nuevo)
for producto in almacen:
    print(f"Stock disponible: {producto} ")
print(f"Marcial, el inventario de Caxias ha sido actualizado. Total: {len(almacen)} tipos.")
almacen.pop(0)
for producto in almacen:
    print(f"Stock disponible: {producto}")