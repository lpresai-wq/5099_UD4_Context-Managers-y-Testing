"""09. pytest.raises también usa with para verificar una excepción esperada."""
import pytest


def calcular_media(notas):
    if not notas:
        raise ValueError("La lista está vacía")
    return sum(notas) / len(notas)


def main():
    # Este context manager NO evita el error para ocultarlo:
    # comprueba que la función lance exactamente el tipo esperado.
    with pytest.raises(ValueError, match="vacía") as informacion:
        calcular_media([])

    print("Prueba correcta: se lanzó ValueError.")
    print("Mensaje de la excepción:", informacion.value)
    print("En tests/test_media.py esta comprobación se ejecuta automáticamente.")


if __name__ == "__main__":
    main()
