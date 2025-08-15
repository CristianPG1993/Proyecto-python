from cargar_preguntas import cargar_preguntas
from guardar_ranking import guardar_resultado


def cargar_cuestionario():
    preguntas = cargar_preguntas()

    aciertos = 0

    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)
        respuesta = input("Elige una respuesta (A, B, C o D): ").strip().upper()
        while respuesta not in ["A", "B", "C", "D"]:
            print("❌ Respuesta no válida. Debes elegir A, B, C o D.")
            respuesta = input("Inténtalo de nuevo: ").strip().upper()
        if respuesta == pregunta["respuesta_correcta"]:
            aciertos += 1
            print("Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es la {pregunta['respuesta_correcta']}.")



    preguntas_totales = len(preguntas)

    porcentaje = (aciertos/preguntas_totales) * 100

    print(f"Porcentaje de aciertos: {porcentaje} %.")

    if porcentaje >= 90:
        print("Excelente, has acertado todas las preguntas.")
    elif porcentaje >= 70:
        print("Muy bien!!")
    elif porcentaje >= 60:
        print("Bien!")
    elif porcentaje >= 50:
        print("Muy justo! Tienes que mejorar.")
    else:
        print("Necesitas empollar más!")



    nombre = input("Introduce tu nombre para guardar el resultado: ")
    guardar_resultado(nombre,porcentaje)