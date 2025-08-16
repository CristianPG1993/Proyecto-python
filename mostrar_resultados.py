
def mostrar_resultados(aciertos: int, total: int) -> float:
    """
    Muestra el resumen final (total, aciertos, % y valoración).
    Devuelve el porcentaje (float) para poder guardarlo en el ranking.
    """
    porcentaje = (aciertos / total) * 100 if total else 0.0

    if porcentaje == 100:
        valoracion = "¡Excelente! Has acertado todas las preguntas."
    elif porcentaje >= 90:
        valoracion = "¡Excelente!"
    elif porcentaje >= 70:
        valoracion = "Muy bien!!"
    elif porcentaje >= 60:
        valoracion = "Bien!"
    elif porcentaje >= 50:
        valoracion = "Muy justo! Tienes que mejorar."
    else:
        valoracion = "Necesitas empollar más!"

    print("\n=== RESULTADOS ===")
    print(f"Total de preguntas: {total}")
    print(f"Aciertos: {aciertos}")
    print(f"Porcentaje de aciertos: {porcentaje:.2f}%")
    print(valoracion)

    return porcentaje
