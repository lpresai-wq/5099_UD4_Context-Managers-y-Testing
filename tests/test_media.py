"""Tests de media: casos normales, valores límite y excepciones."""
import pytest
from src.notas import calcular_media


def test_media_basica():
    assert calcular_media([8, 6, 10]) == 8.0


def test_media_un_elemento():
    assert calcular_media([7]) == 7.0


def test_media_decimales():
    assert calcular_media([7, 8]) == 7.5


def test_media_lista_vacia():
    # pytest.raises comprueba que SE PRODUCE la excepción indicada.
    with pytest.raises(ValueError):
        calcular_media([])


def test_media_lista_vacia_con_mensaje():
    # match añade una comprobación sobre el mensaje de error.
    with pytest.raises(ValueError, match="vacía"):
        calcular_media([])
