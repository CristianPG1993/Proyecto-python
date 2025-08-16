from cargar_preguntas import cargar_preguntas
# Importamos la función 'cargar_preguntas' desde el archivo 'cargar_preguntas.py'

def test_cantidad_preguntas():
    """
    Test que verifica que la función 'cargar_preguntas'
    cargue exactamente 15 preguntas desde el archivo 'preguntas.txt'.
    """
    # Llamamos a la función para obtener la lista de preguntas
    preguntas = cargar_preguntas()

    # Usamos 'assert' para comprobar que el número de preguntas sea 15
    # Si no lo es, se muestra el mensaje de error con el número real obtenido
    assert len(preguntas) == 15, f"Se esperaban 15 preguntas, pero se obtuvieron {len(preguntas)}"

# Bloque principal: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    # Ejecutamos el test
    test_cantidad_preguntas()
    # Si el test pasa, mostramos mensaje de éxito
    print("✅ Test 1 pasado: se cargaron 15 preguntas.")
