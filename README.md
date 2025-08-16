# Generador de Cuestionarios en Python

Aplicación de consola que permite realizar un cuestionario tipo test, corregir las respuestas y guardar los resultados en un ranking.

## Funcionalidades
- Menú con tres opciones:
  1. Empezar cuestionario
  2. Ver ranking
  3. Salir
- Preguntas cargadas desde `preguntas.txt`
- Validación de respuestas (A, B, C o D)
- Cálculo de porcentaje de aciertos y valoración final
- Guardado de resultados en `ranking.txt`

## Archivos importantes
- `main.py`: archivo principal del programa
- `cargar_preguntas.py`: carga las preguntas
- `cargar_cuestionario.py`: ejecuta el cuestionario
- `mostrar_ranking.py`: muestra el ranking
- `guardar_ranking.py`: guarda resultados en el ranking
- `preguntas.txt`: contiene las preguntas
- `ranking.txt`: contiene los resultados



## Formato de preguntas.txt
Cada pregunta ocupa 6 líneas:
1. Enunciado
2. Opción A
3. Opción B
4. Opción C
5. Opción D
6. Respuesta correcta (A, B, C o D)
