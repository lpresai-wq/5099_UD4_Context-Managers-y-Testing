"""05. Leer un archivo línea a línea y quitar los saltos de línea."""
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "datos" / "alumnos.txt"


def main():
    with open(RUTA, "r", encoding="utf-8") as archivo:
        # Cada iteración recupera una línea del archivo.
        for linea in archivo:
            # strip() elimina el salto de línea final y otros espacios extremos.
            print("Registro:", linea.strip())

    print("¿Se cerró el archivo?", archivo.closed)  # True


if __name__ == "__main__":
    main()
