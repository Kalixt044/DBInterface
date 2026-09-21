# Cómo ejecutar las pruebas — Censo Rural

Este documento explica cómo preparar el entorno y ejecutar las pruebas automatizadas del proyecto (versión desktop y web).

1) Preparar un entorno virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate
```

2) Instalar dependencias de desarrollo

```bash
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

3) Estructura de tests creada
- `tests/test_desktop_calculate_age.py` — pruebas unitarias para la lógica de escritorio
- `tests/test_api_endpoints.py` — pruebas básicas de la API (FastAPI TestClient)
- `tests/fixtures/datos_personales_sample.csv` — CSV de ejemplo para pruebas de importación

4) Ejecutar todas las pruebas

```bash
pytest -q
```

5) Ejecutar un solo archivo de pruebas

```bash
pytest -q tests/test_desktop_calculate_age.py
pytest -q tests/test_api_endpoints.py
```

6) Notas específicas
- Las pruebas de la API usan `fastapi.testclient.TestClient` y **no** requieren levantar el servidor.
- Las pruebas del escritorio importan módulos que muestran diálogos (`tkinter.messagebox`). Para evitar pop-ups los tests sustituyen la función `messagebox.showerror` al ejecutar.
- Si `pytest` no está disponible en el sistema, seguir el paso 1 y 2 para crear un entorno aislado e instalar dependencias.

7) Ejecutar pruebas con cobertura (opcional)

```bash
pip install pytest-cov
pytest --cov=./ -q
```

8) Integración continua
- Se añadió el flujo `.github/workflows/ci-tests.yml` que ejecuta `pytest` en push y pull requests.

9) Problemas comunes
- `pytest: command not found`: instale dependencias en un virtualenv o use `python -m pip install -r requirements-dev.txt`.
- Errores de importación: asegúrese de ejecutar los tests desde la raíz del repositorio `/home/mrmonkey/Documents/DBInterface`.

10) Siguientes pasos sugeridos
- Ejecutar `pytest -q` en su entorno local y revisar `tests/` para ampliar casos.
- Si desea, puedo ejecutar las pruebas aquí (requiere instalar dependencias en este entorno). 

---
Archivo creado: [README_RUN_TESTS.md](README_RUN_TESTS.md)
