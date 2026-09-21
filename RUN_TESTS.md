# Cómo ejecutar la suite de pruebas — Censo Rural

Última actualización: 2026-08-30

Este documento explica cómo preparar el entorno, instalar dependencias y ejecutar las pruebas unitarias e de integración para las versiones **desktop** y **web** del proyecto Censo Rural.

1) Requisitos previos
- Sistema operativo: Linux (se recomienda Ubuntu/Fedora).
- Python 3.12+ instalado.
- Acceso a la carpeta del proyecto: `~/Documents/DBInterface` (o donde tengas el repo).

2) Preparar un entorno virtual (recomendado)

```bash
cd /home/mrmonkey/Documents/DBInterface
python -m venv .venv
source .venv/bin/activate
```

Si usas `zsh` o `fish`, ajusta el `source` correspondiente.

3) Instalar dependencias de desarrollo

```bash
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

Si no quieres usar el archivo `requirements-dev.txt`, instala al menos:

```bash
pip install pytest fastapi httpx uvicorn pytest-cov
```

4) Ejecutar la suite completa de tests

```bash
pytest -q
```

5) Ejecutar tests específicos

- Tests de lógica del escritorio (calcular edad):

```bash
pytest -q tests/test_desktop_calculate_age.py
```

- Tests de endpoints API (básicos con TestClient):

```bash
pytest -q tests/test_api_endpoints.py
```

- Ejecutar un test puntual por nombre (ej.: "calcular"):

```bash
pytest -q -k calcular
```

6) Ejecutar cobertura (opcional)

```bash
pip install pytest-cov
pytest --cov=./ -q
```

7) Ejecutar el backend manualmente (para pruebas manuales o con navegador)

```bash
cd ProyectoWeb/Back
uvicorn app.main:app --reload --port 8000
# luego en otra terminal puedes probar con http://127.0.0.1:8000/docs
```

Nota: los tests automáticos para la API incluidos en `tests/test_api_endpoints.py` usan `TestClient` de FastAPI y no requieren arrancar `uvicorn`.

8) Integración continua (GitHub Actions)

El repositorio incluye `.github/workflows/ci-tests.yml` que ejecuta `pytest` en cada `push` o `pull_request` a `main`/`master`. No necesitas acciones locales para CI — solo empuja tus cambios.

9) Problemas comunes y soluciones
- "bash: pytest: command not found": instala dependencias con `pip install -r requirements-dev.txt` o ejecuta `python -m pytest` en su lugar.
- Errores de importación del paquete web: ejecuta `pytest` desde la raíz del proyecto (`/home/mrmonkey/Documents/DBInterface`) para que `sys.path` relativo funcione.
- Tests que abren ventanas GUI: los tests incluidos desactivan diálogos (se sobreescribe `messagebox.showerror`) para evitar bloqueos.

10) Buenas prácticas para ejecutar pruebas
- Ejecuta `pytest -q` en un entorno virtual limpio.
- Antes de ejecutar pruebas de integración, restablece o prepara la base de datos de prueba (SQLite) y limpia `datos_personales.csv` si vas a probar importaciones.
- Documenta resultados y adjunta la salida de `pytest -q` en los artefactos de CI si corresponde.

Si quieres, puedo ejecutar los tests aquí (instalar dependencias y correr pytest) o guiarte paso a paso en tu terminal. ¿Deseas que los ejecute en este entorno ahora?
