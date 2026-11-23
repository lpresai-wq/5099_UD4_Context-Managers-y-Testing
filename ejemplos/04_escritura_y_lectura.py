"""04. Escribir con modo 'w' y leer con modo 'r' utilizando with."""
from pathlib import Path

SALIDAS = Path(__file__).resolve().parent.parent / "salidas"
RUTA = SALIDAS / "notas.txt"


def main():
    SALIDAS.mkdir(exist_ok=True)

    # "w" crea o SOBRESCRIBE el archivo: al repetir el ejemplo no se duplican notas.
    with open(RUTA, "w", encoding="utf-8") as archivo:
        archivo.write("Ana: 7.5\n")
        archivo.write("Luis: 8.0\n")
        print("Mientras se escribe, ¿cerrado?", archivo.closed)  # False

    print("Después de escribir, ¿cerrado?", archivo.closed)  # True

    # Se vuelve a abrir, ahora solo para leer.
    with open(RUTA, "r", encoding="utf-8") as archivo:
        print("Notas guardadas:\n" + archivo.read())

    print("Archivo generado:", RUTA)


if __name__ == "__main__":
    main()
