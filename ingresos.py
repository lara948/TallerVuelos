UMBRAL_DESCUENTO = 500
PORCENTAJE_DESCUENTO = 0.15

def calcular_precio_final(precio):
    if precio > UMBRAL_DESCUENTO:
        return precio * (1 - PORCENTAJE_DESCUENTO)
    return precio

def calcular_ingreso_vuelo(pasajeros, precio):
    return pasajeros * calcular_precio_final(precio)