"""02. Leer un archivo mediante with: cierre automático."""
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "datos" / "datos.txt"


def main():
    try:
        # as asigna el objeto archivo a la variable indicada.
        with open(RUTA, "r", encoding="utf-8") as archivo:
            print("Dentro del with, ¿cerrado?", archivo.closed)  # False
            contenido = archivo.read()
            print("Contenido:\n", contenido, sep="")

        # Al abandonar el with, se ejecuta el cierre automático.
        print("Fuera del with, ¿cerrado?", archivo.closed)  # True
    except FileNotFoundError:
        print("No existe el archivo de datos.")


if __name__ == "__main__":
    main()
