"""Tests de la función es_aprobado, incluidos los límites."""
from src.notas import es_aprobado


def test_aprobado_justo_en_cinco():
    assert es_aprobado(5) is True


def test_suspenso_justo_debajo_de_cinco():
    assert es_aprobado(4.9) is False


def test_aprobado_maximo():
    assert es_aprobado(10) is True


def test_suspenso_cero():
    assert es_aprobado(0) is False
