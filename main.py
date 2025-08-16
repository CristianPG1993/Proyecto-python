from cargar_preguntas import cargar_preguntas
# Importa la función que carga las preguntas desde 'preguntas.txt'

from mostrar_menu import mostrar_menu
# Importa la función que muestra el menú principal en pantalla

from cargar_cuestionario import cargar_cuestionario
# Importa la función que ejecuta el cuestionario

from mostrar_ranking import mostrar_ranking
# Importa la función que muestra el ranking de resultados guardados


def main():
    """
    Función principal del programa.
    Muestra el menú de opciones y ejecuta la acción correspondiente
    según la elección del usuario.
    """

    # Bucle infinito para mantener el programa activo hasta que el usuario decida salir
    while True:
        # Muestra las opciones del menú
        mostrar_menu()

        # Pide al usuario que elija una opción
        opcion = input("Introduce una opción (1 - 3):").strip()

        # Opción 1: ejecutar el cuestionario
        if opcion == "1":
            cargar_cuestionario()

        # Opción 2: mostrar el ranking
        elif opcion == "2":
            mostrar_ranking()

        # Opción 3: salir del programa
        elif opcion == "3":
            print("Vas a salir del menú!")
            break

        # Cualquier otro valor: opción no válida
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecuta la función 'main()' solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
