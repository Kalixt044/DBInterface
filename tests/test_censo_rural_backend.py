import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'ProyectoWeb' / 'Back'))

from app.main import app
from app.routes import crud
from app.services.database import SQLiteCRUDService


@pytest.fixture
def temp_db_service(tmp_path):
    db_path = tmp_path / 'personas_test.db'
    service = SQLiteCRUDService(db_path)
    original_db = crud.db_crud
    crud.db_crud = service
    try:
        yield service
    finally:
        crud.db_crud = original_db


def test_insert_and_get_record(temp_db_service):
    client = TestClient(app)

    payload = {
        'primer_nombres': 'Ana',
        'primer_apellido': 'García',
        'documento': 'CC',
        'numero_identificacion': '1000001',
        'direccion': 'Calle 10 # 20-30',
        'fecha_nacimiento': '2000-05-10',
        'sexo': 'F'
    }

    post_response = client.post('/api/table/personas/insert', json=payload)
    assert post_response.status_code == 200, post_response.text
    body = post_response.json()
    assert body['success'] is True
    assert 'id' in body

    record_id = body['id']
    get_response = client.get(f'/api/table/personas/{record_id}')
    assert get_response.status_code == 200, get_response.text
    data = get_response.json()
    assert data['primer_nombres'] == 'Ana'
    assert data['documento'] == 'CC'


def test_invalid_payload_returns_400(temp_db_service):
    client = TestClient(app)
    response = client.post('/api/table/personas/insert', json={})
    assert response.status_code == 400
    assert 'No se recibieron datos' in response.json()['detail']


def test_missing_record_returns_404(temp_db_service):
    client = TestClient(app)
    response = client.get('/api/table/personas/999999')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Registro no encontrado'


def test_update_and_delete_record(temp_db_service):
    client = TestClient(app)
    payload = {
        'primer_nombres': 'Luis',
        'primer_apellido': 'Rojas',
        'documento': 'TI',
        'numero_identificacion': '1000002',
        'direccion': 'Carrera 5',
        'fecha_nacimiento': '1995-11-15',
        'sexo': 'M'
    }

    create_response = client.post('/api/table/personas/insert', json=payload)
    assert create_response.status_code == 200
    record_id = create_response.json()['id']

    update_response = client.put(
        f'/api/table/personas/{record_id}',
        json={'primer_nombres': 'Luis Alberto', 'primer_apellido': 'Rojas'}
    )
    assert update_response.status_code == 200, update_response.text
    assert update_response.json()['success'] is True

    get_response = client.get(f'/api/table/personas/{record_id}')
    assert get_response.status_code == 200
    assert get_response.json()['primer_nombres'] == 'Luis Alberto'

    delete_response = client.delete(f'/api/table/personas/{record_id}')
    assert delete_response.status_code == 200
    assert delete_response.json()['success'] is True

    verify_response = client.get(f'/api/table/personas/{record_id}')
    assert verify_response.status_code == 404
