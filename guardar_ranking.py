def guardar_resultado(nombre, porcentaje):
    with open("ranking.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre}, {porcentaje}\n")