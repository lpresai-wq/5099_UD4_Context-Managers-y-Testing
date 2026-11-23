"""FASE REFACTORIZAR: mejorar la claridad sin cambiar el resultado."""


def es_aprobado(nota):
    """Indica si una calificación alcanza el mínimo para aprobar."""
    nota_minima_aprobado = 5
    return nota >= nota_minima_aprobado


def test_es_aprobado():
    assert es_aprobado(5) is True
    assert es_aprobado(4.9) is False
    assert es_aprobado(10) is True
    assert es_aprobado(0) is False
