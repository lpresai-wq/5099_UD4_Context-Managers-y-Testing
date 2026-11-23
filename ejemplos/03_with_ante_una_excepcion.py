"""03. Demostrar que with cierra el archivo aunque int() genere ValueError."""
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "datos" / "numero_no_valido.txt"


def main():
    archivo = None
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            print("Contenido leído:", contenido)
            numero = int(contenido)  # Con 'hola', se produce ValueError.
            print("Número convertido:", numero)  # No se ejecuta si falla int().
    except ValueError:
        print("No se puede convertir el contenido a número entero.")
    except FileNotFoundError:
        print("No existe el archivo de entrada.")

    # Si se abrió, with lo cerró antes de que except gestionara ValueError.
    if archivo is not None:
        print("¿Archivo cerrado tras el error?", archivo.closed)  # True


if __name__ == "__main__":
    main()
