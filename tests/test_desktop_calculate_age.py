import os
import sys

# Ensure DesktopProyect is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DesktopProyect')))

import index

# Prevent GUI dialogs during tests
try:
    index.messagebox.showerror = lambda *a, **k: None
except Exception:
    pass


def test_calcular_edad_valida():
    # La implementación actual usa fecha fija 2024-11-27 como 'hoy'
    # Para nacimiento 01/01/2000 la edad esperada es 24
    assert index.calcular_edad("01/01/2000") == 24


def test_calcular_edad_invalida():
    # Formato inválido debe retornar None (y no lanzar excepción)
    assert index.calcular_edad("2000-01-01") is None
