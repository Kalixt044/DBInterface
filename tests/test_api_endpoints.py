import os
import sys

# Ensure ProyectoWeb/Back is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ProyectoWeb', 'Back')))

from fastapi.testclient import TestClient

try:
    from app.main import app
except Exception:
    # If import fails, raise so tests surface the error
    raise

client = TestClient(app)


def test_root_endpoint():
    r = client.get("/")
    assert r.status_code == 200
    assert "API funcionando" in r.json().get("message", "")


def test_list_tables_endpoint():
    r = client.get("/api/tables")
    assert r.status_code == 200
    assert isinstance(r.json(), dict)
