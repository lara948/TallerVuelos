def ordenar_por_ingreso(resultados):
    return sorted(
        resultados.items(),
        key=lambda item: item[1]["ingreso"],
        reverse=True
    )

def calcular_ingreso_global(resultados):
    return sum(datos["ingreso"] for datos in resultados.values())

def imprimir_reporte(resultados):
    ordenados = ordenar_por_ingreso(resultados)

    print("\nREPORTE DE VUELOS")

    for codigo, d in ordenados:
        print("-" * 40)
        print("Vuelo:", codigo)
        print("Pasajeros:", d["pasajeros"])
        print("Precio original:", d["precio_original"])
        print("Precio final:", d["precio_final"])
        print("Ingreso:", d["ingreso"])
        print(
            "Baja ocupación:",
            "Sí" if d["baja_ocupacion"] else "No"
        )

    print("-" * 40)
    print("Ingreso total global:",
          calcular_ingreso_global(resultados))