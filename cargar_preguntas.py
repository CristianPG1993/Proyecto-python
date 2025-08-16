def cargar_preguntas():
    """
    Función que lee el archivo 'preguntas.txt' y devuelve
    una lista de diccionarios con las preguntas, opciones
    y la respuesta correcta.
    """

    # Lista vacía donde se guardarán todas las preguntas
    preguntas = []

    # Abrimos el archivo 'preguntas.txt' en modo lectura con codificación UTF-8
    # Usamos 'with' para cerrar el archivo automáticamente al terminar
    with open("preguntas.txt", "r", encoding="utf-8") as archivo:
        # Leemos todas las líneas y las guardamos en una lista
        lineas = archivo.readlines()

    # Recorremos la lista de líneas saltando de 6 en 6
    # (1 línea para la pregunta, 4 para las opciones, 1 para la respuesta correcta)
    for i in range(0, len(lineas), 6):
        # Guardamos la pregunta eliminando espacios y saltos de línea
        pregunta = lineas[i].strip()

        # Guardamos las 4 opciones, eliminando espacios y saltos
        opciones = [
            lineas[i+1].strip(),
            lineas[i+2].strip(),
            lineas[i+3].strip(),
            lineas[i+4].strip()
        ]

        # Guardamos la respuesta correcta (por ejemplo: "A", "B", "C" o "D")
        respuesta_correcta = lineas[i+5].strip()

        # Creamos un diccionario con la estructura de la pregunta
        preguntas.append({
            "pregunta": pregunta,
            "opciones": opciones,
            "respuesta_correcta": respuesta_correcta
        })

    # Devolvemos la lista de preguntas
    return preguntas
