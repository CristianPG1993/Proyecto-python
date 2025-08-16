def obtener_respuesta() -> str:
    """
    Pide una respuesta al usuario (A/B/C/D) y valida hasta que sea correcta.
    Devuelve la letra en mayúsculas.
    """
    respuesta = input("Elige una respuesta (A, B, C o D): ").strip().upper()
    while respuesta not in ("A", "B", "C", "D"):
        print("❌ Respuesta no válida. Debes elegir A, B, C o D.")
        respuesta = input("Inténtalo de nuevo: ").strip().upper()
    return respuesta


