"""01. Cierre manual con try/finally: punto de partida del PDF."""
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "datos" / "datos.txt"


def main():
    # Antes de usar with, era frecuente gestionar el cierre con finally.
    archivo = None
    try:
        archivo = open(RUTA, "r", encoding="utf-8")
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
    except FileNotFoundError:
        print("No se ha encontrado el archivo de datos.")
    finally:
        # finally se ejecuta tanto si la lectura tuvo éxito como si falló.
        if archivo is not None:
            archivo.close()
            print("¿Está cerrado?", archivo.closed)  # True


if __name__ == "__main__":
    main()
