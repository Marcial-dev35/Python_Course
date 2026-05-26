def calculo_salario(horas, salario_hora):
    salario_total = horas * salario_hora
    return salario_total

sueldo = calculo_salario(85, 300)
print(f"Mi salario total es {sueldo} dolares.")
