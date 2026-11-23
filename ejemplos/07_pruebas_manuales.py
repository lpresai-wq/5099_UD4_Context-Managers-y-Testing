"""07. Antes de pytest: observar resultados manualmente con print()."""


def calcular_media(notas):
    return sum(notas) / len(notas)


def main():
    print("Media [8, 6, 10]:", calcular_media([8, 6, 10]))  # Se espera 8.0
    print("Media [7]:", calcular_media([7]))               # Se espera 7.0

    # Estas salidas NO se verifican solas: una persona debe compararlas.
    # En tests/test_media.py se automatiza usando assert y pytest.
    print("Comparar visualmente los resultados esperados y obtenidos.")


if __name__ == "__main__":
    main()
