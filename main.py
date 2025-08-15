from cargar_preguntas import cargar_preguntas
from mostrar_menu import mostrar_menu
from cargar_cuestionario import cargar_cuestionario
from mostrar_ranking import mostrar_ranking


def main():
    while True:
        mostrar_menu()
        opcion = input("Introduce una opción (1 - 3):").strip()

        if opcion == "1":
            cargar_cuestionario()
        elif opcion == "2":
            mostrar_ranking()
        elif opcion == "3":
            print("Vas a salir del menú!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()


