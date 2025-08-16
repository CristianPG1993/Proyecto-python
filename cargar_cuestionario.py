from cargar_preguntas import cargar_preguntas
# Importamos la función para cargar las preguntas desde 'preguntas.txt'

from guardar_ranking import guardar_resultado
# Importamos la función para guardar el resultado en 'ranking.txt'

from obtener_respuesta import obtener_respuesta
# Importamos la función para obtener la respuesta correcta

from mostrar_resultados import mostrar_resultados
# Importamos la función para obtener los resultados



def cargar_cuestionario():
    """
    Función que ejecuta el cuestionario:
    - Carga las preguntas desde un archivo.
    - Muestra las preguntas y opciones al usuario.
    - Valida y corrige las respuestas.
    - Calcula el porcentaje de aciertos.
    - Muestra un mensaje de valoración final.
    - Guarda el resultado en el ranking.
    """

    # Cargamos las preguntas en una lista de diccionarios
    preguntas = cargar_preguntas()

    # Contador de respuestas correctas
    aciertos = 0

    # Bucle principal: recorre cada pregunta del cuestionario
    for pregunta in preguntas:
        # Mostramos el enunciado de la pregunta
        print(pregunta["pregunta"])

        # Mostramos las opciones de respuesta
        for opcion in pregunta["opciones"]:
            print(opcion)

        # Solicitamos la respuesta al usuario, quitando espacios y en mayúscula llamando a obtener_respuesta()
        respuesta = obtener_respuesta()



        # Comprobamos si la respuesta es correcta
        if respuesta == pregunta["respuesta_correcta"]:
            aciertos += 1
            print("Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es la {pregunta['respuesta_correcta']}.")


    # Calculamos el porcentaje de aciertos
    porcentaje = mostrar_resultados(aciertos,len(preguntas))

    # Pedimos el nombre para guardar el resultado en el ranking
    nombre = input("Introduce tu nombre para guardar el resultado: ")

    # Guardamos el resultado en el archivo 'ranking.txt'
    guardar_resultado(nombre, porcentaje)
