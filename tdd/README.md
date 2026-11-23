# Demostración de TDD: ROJO → VERDE → REFACTORIZAR

**Problema:** construir `es_aprobado(nota)`, que devuelve `True` si la nota es 5 o superior, y `False` en otro caso.

La misma actividad aparece en tres carpetas para observar el proceso paso a paso:

1. **ROJO:** la función devuelve siempre `False` (incompleta). El test de `5` **debe fallar**.
2. **VERDE:** se implementa `return nota >= 5`. Todos los tests **pasan**.
3. **REFACTORIZAR:** se mejora la legibilidad, utilizando una constante y una cadena de documentación, sin cambiar el comportamiento. Los tests **siguen pasando**.

Desde la raíz del repositorio, ejecutar **por separado**:

```bash
python -m pytest tdd/01_rojo/test_es_aprobado.py -v
python -m pytest tdd/02_verde/test_es_aprobado.py -v
python -m pytest tdd/03_refactorizar/test_es_aprobado.py -v
```

**Importante:** la carpeta `01_rojo/` contiene un fallo *intencionado*. El archivo `pytest.ini` limita la ejecución habitual (`python -m pytest -v`) a `tests/`, para no incluirlo accidentalmente.

**Propuesta de aprendizaje:** abrir primero el archivo ROJO, predecir qué test fallará y ejecutarlo. A continuación, compararlo con VERDE y REFACTORIZAR. La idea es comprender el proceso, no solo obtener el resultado final.
