def mostrar_ranking():
    """
    Función que lee un archivo llamado 'ranking.txt',
    ordena los resultados de mayor a menor porcentaje
    y los muestra en pantalla.
    """

    # Abrimos el archivo 'ranking.txt' en modo lectura con codificación UTF-8
    # Usamos 'with' para que el archivo se cierre automáticamente al terminar
    with open("ranking.txt", "r", encoding="utf-8") as archivo:
        # Leemos todas las líneas del archivo en una lista
        lineas = archivo.readlines()

        # Lista donde guardaremos las tuplas (nombre, porcentaje)
        ranking = []

        # Procesamos cada línea del archivo
        for linea in lineas:
            # Eliminamos espacios y saltos de línea, luego separamos por coma
            nombre, porcentaje = linea.strip().split(",")
            # Convertimos el porcentaje a tipo float
            porcentaje = float(porcentaje)
            # Añadimos el par (nombre, porcentaje) a la lista
            ranking.append((nombre.strip(), porcentaje))

        # Ordenamos manualmente la lista usando el algoritmo de burbuja
        # Esto recorre varias veces la lista, intercambiando elementos
        for i in range(len(ranking)):
            for j in range(len(ranking) - 1):
                # Comparamos el porcentaje actual con el siguiente
                if ranking[j][1] < ranking[j + 1][1]:
                    # Si el siguiente es mayor, intercambiamos posiciones
                    ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

        # Mostramos el ranking ordenado
        print("\n Ranking ordenado:")
        # Enumeramos la lista desde 1, mostrando nombre y porcentaje con 2 decimales
        for i, (nombre, porcentaje) in enumerate(ranking, start=1):
            print(f"{i}. {nombre} - {porcentaje:.2f}%")
