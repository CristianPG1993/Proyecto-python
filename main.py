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

def mostrar_menu():
    print("\n### MENÚ ###")
    print("1 - Empezar cuestionario")
    print("2 - Ranking")
    print("3 - Salir")

def cargar_cuestionario():
    print("Aquí se introducirá la lógica con las preguntas")

def mostrar_ranking():
    print("\n[INFO] El ranking se implementará más adelante.")


def main():
    while True:
        mostrar_menu()


        opcion = input("Introduce una opción (1 - 3):").strip()

        if opcion == "1":
            cargar_cuestionario()
            preguntas = cargar_preguntas()
            print(f"Se han cargado {len(preguntas)} preguntas.")
            print(preguntas[0])  # muestra la primera como ejemplo
        elif opcion == "2":
            mostrar_ranking()
        elif opcion == "3":
            print("Vas a salir del menú!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")





if __name__ == "__main__":
    main()


