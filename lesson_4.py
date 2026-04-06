temperatura = float(input("Cual es la temperatura actual de la cortadora de plasma?: "))
if temperatura > 150:
    print("PELIGRO: Apagado de emergencia inmediato.")
elif temperatura >= 100:
    print("Aviso: Temperatura elevada, revisar refrigeracion.")
else:
    print("Estado: Operaciuon normal.")