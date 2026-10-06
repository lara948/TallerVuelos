from ingresos import calcular_precio_final, calcular_ingreso_vuelo

LIMITE_BAJA_OCUPACION = 50

def es_baja_ocupacion(pasajeros):
    return pasajeros < LIMITE_BAJA_OCUPACION

def procesar_vuelos(vuelos):
    resultados = {}

    for codigo, info in vuelos.items():
        pasajeros = info["pasajeros"]
        precio = info["precio"]

        resultados[codigo] = {
            "pasajeros": pasajeros,
            "precio_original": precio,
            "precio_final": calcular_precio_final(precio),
            "ingreso": calcular_ingreso_vuelo(pasajeros, precio),
            "baja_ocupacion": es_baja_ocupacion(pasajeros),
        }

    return resultados