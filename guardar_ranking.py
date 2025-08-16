def guardar_resultado(nombre, porcentaje):
    """
    Función que guarda el nombre y el porcentaje de aciertos
    en el archivo 'ranking.txt', añadiendo el registro al final.

    Parámetros:
        nombre (str): Nombre del participante.
        porcentaje (float o int): Porcentaje de aciertos.
    """

    # Abrimos el archivo 'ranking.txt' en modo "append" (a)
    # para añadir datos al final sin borrar el contenido previo.
    # Usamos UTF-8 para permitir caracteres especiales.
    with open("ranking.txt", "a", encoding="utf-8") as archivo:
        # Escribimos una línea con el formato: nombre, porcentaje
        # Añadimos salto de línea al final para que cada registro esté en una línea distinta.
        archivo.write(f"{nombre}, {porcentaje}\n")
