

def mostrar_ranking():
    with open("ranking.txt", "r", encoding="utf-8")as archivo:
        lineas = archivo.readlines()

        ranking = []

        for linea in lineas:
            nombre, porcentaje = linea.strip().split(",")
            porcentaje = float(porcentaje)
            ranking.append((nombre.strip(), porcentaje))



        for i in range(len(ranking)):
            for j in range(len(ranking) - 1):
                if ranking[j][1] < ranking[j + 1][1]:
                    ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]




        print("\n Ranking ordenado:")
        for i, (nombre, porcentaje) in enumerate(ranking, start=1):
            print(f"{i}. {nombre} - {porcentaje:.2f}%")









