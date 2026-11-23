"""08. La función lanza ValueError si la lista de notas está vacía."""


def calcular_media(notas):
    if not notas:
        raise ValueError("La lista está vacía")
    return sum(notas) / len(notas)


def main():
    print("Media correcta:", calcular_media([8, 6, 10]))  # 8.0

    try:
        calcular_media([])
    except ValueError as error:
        print("Excepción capturada:", error)

    # El test automatizado de este caso está en tests/test_media.py.


if __name__ == "__main__":
    main()
