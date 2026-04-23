# --- Base de Datos de la Planta ---
metalurgica = {
    "Horno_A": {
        "operario": "Marcial",
        "temperatura": 850,
        "estado": "Activo"
    },
    "Prensa_B": {
        "operario": "Jose",
        "presion": 120,
        "estado": "Apagada"
    }
}

# --- TUS TAREAS COMIENZAN AQUÍ ---

# Tarea 1 (Read): Imprime un mensaje que diga la temperatura actual del Horno_A.
# Tip: Recuerda usar la doble llave metalurgica["..."]["..."]

# Tarea 2 (Update): Jose por fin llegó a su turno. Cambia el estado de la Prensa_B a "Activa".

# Tarea 3 (Create): Acabas de terminar un lote. Añade una nueva llave al Horno_A llamada "piezas_terminadas" con el valor 500.

# Reporte final: Imprime el diccionario completo para ver los cambios.
print(f"La temperatura actual del Horno_A es: {metalurgica['Horno_A']['temperatura']}")
metalurgica["Prensa_B"]['estado'] = "Activada"
metalurgica["Horno_A"]['piezas_terminadas'] = 500
print(metalurgica)