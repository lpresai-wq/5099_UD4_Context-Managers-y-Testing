# UD4.2 — Context Managers y Testing en Python

**Módulo 5099 · Estructuras de Control en Python (ECP)**  
**UD4 · Gestión de excepciones y código robusto**  
**Contenidos:** `with` y gestión de archivos · `assert` · pruebas con `pytest` · `pytest.raises()` · TDD.

## 1. Antes de empezar: preparar el proyecto

Este repositorio contiene ejemplos **independientes**. Se recomienda ejecutarlos **en el orden numerado**, observar la salida y leer los comentarios que acompañan a cada programa.

### Paso 1. Descargar y abrir

1. Descargar el repositorio desde GitHub (**Code → Download ZIP**).
2. **Descomprimirlo**, manteniendo sus carpetas y archivos.
3. Abrir **VS Code → Archivo → Abrir carpeta** y seleccionar `5099_UD4_2_Context_Managers_y_Testing`.
4. Abrir **Terminal → Nuevo terminal** dentro de VS Code.

**Todos los comandos de esta guía se ejecutan desde la carpeta principal del proyecto**, la que contiene `README.md`, `requirements.txt` y `pytest.ini`.

Comprobar:

```bash
python --version
```

Debe aparecer la versión de Python instalada. Se recomienda **Python 3.10 o superior**.

> En Windows, si `python` no funciona, puede utilizarse `py`. En macOS o Linux, si es necesario, sustituir `python` por `python3` en los comandos.

### Paso 2. Crear el entorno virtual (obligatorio)

**Antes de instalar las dependencias, hay que crear un entorno virtual** en la carpeta principal del proyecto. De esta manera, `pytest` se instalará para este repositorio sin modificar las dependencias de otros proyectos de Python.

**Windows (PowerShell o Símbolo del sistema):**

```powershell
python -m venv .venv
```

Si en Windows el comando `python` no funciona, utilizar:

```powershell
py -m venv .venv
```

**Linux y macOS:**

```bash
python3 -m venv .venv
```

La carpeta `.venv/` se crea automáticamente dentro del proyecto. **No se debe subir a GitHub**: ya está incluida en `.gitignore`.

### Paso 3. Activar el entorno virtual (obligatorio)

Una vez creado, **activar el entorno desde el mismo terminal** que se utilizará para instalar y ejecutar las pruebas.

**Windows — PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows — Símbolo del sistema (CMD):**

```bat
.venv\Scripts\activate.bat
```

**Linux y macOS:**

```bash
source .venv/bin/activate
```

Al activarlo, normalmente aparece `(.venv)` al principio de la línea del terminal. Esto indica que los comandos `python` y `pip` utilizarán el entorno del proyecto.

> **Windows y PowerShell:** si la política de ejecución bloquea `Activate.ps1`, se puede abrir un terminal **CMD** en VS Code y utilizar `.venv\Scripts\activate.bat`. No hace falta modificar las políticas de seguridad del equipo.

> **Recordatorio:** cada vez que se abra un terminal nuevo para trabajar con este repositorio, habrá que **volver a activar el entorno virtual**. No es necesario crearlo otra vez.

### Paso 4. Instalar las dependencias dentro del entorno virtual

**Con `(.venv)` activado**, ejecutar:

```bash
python -m pip install -r requirements.txt
```

El archivo `requirements.txt` indica que se necesita `pytest`.

### Paso 5. Comprobar que pytest funciona

```bash
python -m pytest --version
```

Si se muestra la versión de `pytest`, el entorno está preparado.

**¿Para qué sirve?** Los ejemplos `01` a `08` solo necesitan Python. El ejemplo `09` y las pruebas de las carpetas `tests/` y `tdd/` necesitan `pytest`.

**A partir de aquí, todos los comandos de esta guía se ejecutan con el entorno virtual activado.**

Cuando se termine de trabajar, se puede salir del entorno con:

```bash
deactivate
```

---

## 2. Ejecutar los ejemplos uno a uno

Abrir cada archivo en VS Code, leer sus comentarios y ejecutar el comando indicado en el terminal. **No hace falta modificar el código para que funcione.**

### Bloque A — Context Managers y archivos (`01` a `05`)

| Nº | Ejemplo | Comando para ejecutar | ¿Qué debe observarse? |
|---|---|---|---|
| **01** | Cierre manual con `try/finally` | `python ejemplos/01_cierre_manual_try_finally.py` | Se lee `datos/datos.txt` y se muestra `¿Está cerrado? True`. |
| **02** | Apertura con `with` | `python ejemplos/02_lectura_archivo_con_with.py` | Dentro de `with` aparece `False`; al salir, `True`. |
| **03** | `with` ante una excepción | `python ejemplos/03_with_ante_una_excepcion.py` | Se produce un `ValueError` controlado y el archivo queda cerrado (`True`). |
| **04** | Escritura y lectura | `python ejemplos/04_escritura_y_lectura.py` | Se crea/sobrescribe `salidas/notas.txt` con Ana y Luis y después se lee. |
| **05** | Lectura línea a línea | `python ejemplos/05_lectura_linea_a_linea.py` | Aparece cada registro de `datos/alumnos.txt`, sin el salto de línea final. |

**Prácticas para comprobar que se ha entendido:**

- **01 y 02:** comparar cuántas instrucciones son necesarias para cerrar correctamente el archivo. En el ejemplo 02, comprobar los valores de `archivo.closed`.
- **03:** abrir `datos/numero_no_valido.txt`, observar su contenido y sustituir temporalmente `hola` por `123`. Volver a ejecutar y comprobar que ya no se produce `ValueError`. Restaurar el contenido original después.
- **04:** ejecutar dos veces. Abrir `salidas/notas.txt` y comprobar que los registros **no se duplican**, porque el modo `"w"` sobrescribe el archivo.
- **05:** observar por qué `strip()` elimina los saltos de línea de cada registro.

**Atención:** `04_escritura_y_lectura.py` escribe realmente el archivo `salidas/notas.txt`. Es normal que esta carpeta aparezca después de ejecutar el programa.

### Bloque B — Aserciones, comprobaciones y excepciones (`06` a `09`)

| Nº | Ejemplo | Comando para ejecutar | ¿Qué debe observarse? |
|---|---|---|---|
| **06** | `assert` y `AssertionError` | `python ejemplos/06_assert_y_assertionerror.py` | La primera aserción pasa; la segunda falla **intencionadamente** y se captura para mostrar el mensaje. |
| **07** | Pruebas manuales | `python ejemplos/07_pruebas_manuales.py` | Se muestran las medias `8.0` y `7.0`; hay que comprobarlas visualmente. |
| **08** | Validación con `raise` | `python ejemplos/08_raise_en_calcular_media.py` | Una lista normal devuelve `8.0`; una lista vacía genera `ValueError`, que se captura. |
| **09** | `pytest.raises()` como `with` | `python ejemplos/09_pytest_raises_es_un_context_manager.py` | Se comprueba que aparece el `ValueError` esperado y que su mensaje incluye `vacía`. |

**Prácticas recomendadas:**

- **06:** localizar las dos instrucciones `assert`. Explicar por qué una pasa y la otra falla. El programa termina normalmente porque el fallo esperado se captura con `except AssertionError`.
- **07:** comparar las salidas de `print()` con los resultados esperados. ¿Quién comprueba aquí que el resultado es correcto?
- **08:** observar que `raise` **lanza** una excepción y `except` la **captura**.
- **09:** comprobar que `pytest.raises(ValueError, match="vacía")` no sirve para ocultar el error, sino para **verificar que se produce**.

> **Importante:** los archivos `01` a `09` son programas de demostración. Se ejecutan con `python ejemplos/NOMBRE.py`. Los tests de la siguiente sección se ejecutan de otra manera: con `python -m pytest`.

---

## 3. Ejecutar las pruebas automáticas con pytest

En las pruebas automáticas **no hace falta leer el resultado de cada `print()` para decidir si está bien**: el propio programa comprueba las condiciones mediante `assert`.

Los archivos del repositorio son:

- `src/notas.py`: funciones que se van a comprobar (`calcular_media()` y `es_aprobado()`).
- `tests/test_media.py`: pruebas de la media, incluyendo una lista vacía.
- `tests/test_aprobado.py`: pruebas de calificaciones aprobadas y suspensas.

### 3.1. Ejecutar todas las pruebas normales

```bash
python -m pytest -v
```

**Resultado esperado:** **9 pruebas superadas (`9 passed`)**. Se mostrarán líneas marcadas como `PASSED`.

### 3.2. Ejecutar solo las pruebas de la media

```bash
python -m pytest tests/test_media.py -v
```

**Resultado esperado:** **5 pruebas superadas (`5 passed`)**.

### 3.3. Ejecutar solo las pruebas de aprobado/suspenso

```bash
python -m pytest tests/test_aprobado.py -v
```

**Resultado esperado:** **4 pruebas superadas (`4 passed`)**.

### 3.4. Ejecutar una sola prueba

```bash
python -m pytest tests/test_media.py::test_media_basica -v
```

**Resultado esperado:** **1 prueba superada (`1 passed`)**.

### 3.5. Entender cómo se prueba una excepción

Abrir `tests/test_media.py` y localizar:

```python
import pytest
from src.notas import calcular_media


def test_media_lista_vacia():
    with pytest.raises(ValueError):
        calcular_media([])
```

El test **pasa precisamente porque** `calcular_media([])` lanza el `ValueError` esperado. Si no se produjera esa excepción, el test fallaría.

Para ejecutar únicamente esta comprobación:

```bash
python -m pytest tests/test_media.py::test_media_lista_vacia -v
```

---

## 4. Ejecutar las tres fases de TDD

**TDD** (*Test-Driven Development*) significa desarrollo guiado por pruebas. Se estudiará con la función `es_aprobado(nota)`, que debe devolver `True` si la nota es al menos `5`.

Cada fase tiene su propio archivo. Se ejecutan **por separado**, en este orden:

### Fase 1. ROJO — La prueba debe fallar

```bash
python -m pytest tdd/01_rojo/test_es_aprobado.py -v
```

**Resultado esperado: `1 failed`.** Esto **no es un error del repositorio**: la implementación todavía devuelve siempre `False`, así que falla cuando la nota es `5`.

Leer el mensaje de pytest: muestra qué valor se esperaba (`True`) y cuál se ha obtenido (`False`).

### Fase 2. VERDE — La prueba debe pasar

```bash
python -m pytest tdd/02_verde/test_es_aprobado.py -v
```

**Resultado esperado: `1 passed`.** La función ya utiliza la condición `nota >= 5`.

### Fase 3. REFACTORIZAR — Mejorar manteniendo las pruebas en verde

```bash
python -m pytest tdd/03_refactorizar/test_es_aprobado.py -v
```

**Resultado esperado: `1 passed`.** La función es más legible y conserva el mismo comportamiento.

**Idea principal:** en TDD primero se comprueba que la prueba detecta el fallo, después se escribe el código para superarla y finalmente se mejora el código sin cambiar sus resultados.

Se puede consultar la explicación adicional en [`tdd/README.md`](tdd/README.md).

---

## 5. Carpetas y archivos auxiliares: no es necesario estudiarlos ahora

| Elemento | ¿Para qué está? | ¿Hay que modificarlo? |
|---|---|---|
| `datos/` | Contiene los archivos que leen los ejemplos. | **No**, salvo en las pruebas propuestas, y después restaurar su contenido. |
| `salidas/` | Guarda el resultado del ejemplo 04. | **No**. Puede crearse al ejecutar el programa. |
| `.venv/` | Entorno virtual del proyecto: contiene su propio Python y las dependencias instaladas. | **No**. Se crea con `python -m venv .venv` y no se sube a GitHub. |
| `requirements.txt` | Indica que hay que instalar `pytest` dentro del entorno virtual. | **No**. |
| `pytest.ini` | Hace que la orden general de pytest busque tests en `tests/` y no ejecute automáticamente el fallo intencionado de TDD. | **No**. |
| `Path(__file__).resolve()` | Permite encontrar los archivos del proyecto aunque cambie la ubicación de la carpeta. | **No**. |
| `.gitignore` | Evita subir archivos temporales y otras carpetas que no forman parte de los ejemplos. | **No**. |


---

## 6. Si algo no funciona

| Problema | Comprobación o solución |
|---|---|
| `python` no se reconoce | Probar `py` (Windows) o `python3` (Linux/macOS) y comprobar que Python está instalado. |
| `No module named pytest` | Activar `.venv` y ejecutar `python -m pip install -r requirements.txt`. |
| No aparece `(.venv)` en el terminal | Activar el entorno virtual con el comando indicado en el **paso 3**. |
| PowerShell bloquea `Activate.ps1` | Abrir un terminal **CMD** en VS Code y activar con `.venv\Scripts\activate.bat`. |
| `No such file or directory` al ejecutar un ejemplo | Abrir el terminal **en la raíz del proyecto**, no dentro de `ejemplos/` ni `tests/`. |
| `1 failed` al ejecutar `tdd/01_rojo` | **Es el resultado correcto** de esa fase: se está demostrando el ciclo TDD. |
| Fallan pruebas que deberían pasar | Comprobar que no se han modificado los archivos originales; volver a descomprimir el ZIP si fuera necesario. |
| No aparece `salidas/notas.txt` | Ejecutar el ejemplo **04** y buscar la carpeta `salidas/` en la raíz. |

---

## 7. Resumen de comandos para practicar

**Antes de practicar**, si se ha abierto un terminal nuevo, activar `.venv` con el comando del **paso 3**.

Ejecutar un ejemplo individual:

```bash
python ejemplos/02_lectura_archivo_con_with.py
```

Ejecutar los tests normales:

```bash
python -m pytest -v
```

Ejecutar solo un archivo de tests:

```bash
python -m pytest tests/test_media.py -v
```

Ejecutar las tres fases de TDD:

```bash
python -m pytest tdd/01_rojo/test_es_aprobado.py -v
python -m pytest tdd/02_verde/test_es_aprobado.py -v
python -m pytest tdd/03_refactorizar/test_es_aprobado.py -v
```

> **Recordatorio:** los programas `ejemplos/*.py` se ejecutan con `python`; las pruebas `tests/test_*.py` y `tdd/*/test_*.py`, con `python -m pytest`.

## Recursos

- [Python: la sentencia `with`](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
- [Documentación de pytest](https://docs.pytest.org/en/stable/getting-started.html)
- Material de la unidad: **UD4.2 — Context Managers y Testing**.
