def cargar_preguntas():

    preguntas = []

    with open("preguntas.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    for i in range(0, len(lineas), 6):
        pregunta = lineas[i].strip()
        opciones = [lineas[i+1].strip(),lineas[i+2].strip(),lineas[i+3].strip(),lineas[i+4].strip()]
        respuesta_correcta = lineas[i+5].strip()

        preguntas.append({
            "pregunta": pregunta,
            "opciones": opciones,
            "respuesta_correcta": respuesta_correcta
        })
    return preguntas