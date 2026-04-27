lote_produccion = [
    {"codigo": "A1", "defectos": 3},
    {"codigo": "B2", "defectos": 0},
    {"codigo": "C3", "defectos": 1}
]
for lote in lote_produccion:
    for clave, valor in lote.items():
        print(f"Clave: {clave}, Valor: {valor}")
        if clave == "defectos" and valor > 0:
            print(f"El lote {lote['codigo']} tiene {valor} defectos.")
