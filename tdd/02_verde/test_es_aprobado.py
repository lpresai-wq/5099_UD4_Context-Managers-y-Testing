"""FASE VERDE: código mínimo que hace pasar las comprobaciones."""


def es_aprobado(nota):
    return nota >= 5


def test_es_aprobado():
    assert es_aprobado(5) is True
    assert es_aprobado(4.9) is False
    assert es_aprobado(10) is True
    assert es_aprobado(0) is False
