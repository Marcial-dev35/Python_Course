usuario_autorizado = "marcial"
pin_seguridad = 1234
usuario_autorizado = input("Cual es tu nombre?:" ).lower()
pin_seguridad = int(input("Introduce tu PIN: "))
if usuario_autorizado == "marcial" and pin_seguridad == 1234:
    print("Acceso concedido. Bienvenido al sistema, Marcial")
else:
    print("ERROR: Usuario o PIN incorrectos. Acceso denegado.")