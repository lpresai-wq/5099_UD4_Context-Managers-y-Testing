"""Funciones de la aplicación que se comprueban con pytest."""


def calcular_media(notas):
    """Devuelve la media; rechaza una lista vacía mediante ValueError."""
    if not notas:
        raise ValueError("La lista está vacía")
    return sum(notas) / len(notas)


def es_aprobado(nota):
    """Devuelve True si la calificación es al menos 5."""
    return nota >= 5
