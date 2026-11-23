"""06. Comprobaciones automáticas con assert (introducción)."""


def main():
    # Si la expresión es verdadera, no se lanza ninguna excepción.
    assert 2 + 2 == 4
    print("Primera comprobación: correcta.")

    try:
        # Provocamos un fallo a propósito para observar AssertionError.
        assert 2 + 2 == 5, "La suma no da 5"
    except AssertionError as error:
        print("Segunda comprobación: ha fallado como se esperaba.")
        print("Mensaje de la aserción:", error)

    # En pytest normalmente NO capturamos AssertionError manualmente:
    # dejamos que pytest lo detecte y señale el test que falla.
    print("Fin del ejemplo.")


if __name__ == "__main__":
    main()
