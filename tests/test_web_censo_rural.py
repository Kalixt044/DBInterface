import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'ProyectoWeb' / 'Back'))

from app.main import app
from app.routes import crud
from app.services.database import SQLiteCRUDService


@pytest.fixture
def web_db_service(tmp_path):
    db_path = tmp_path / 'personas_web_test.db'
    service = SQLiteCRUDService(db_path)
    original_db = crud.db_crud
    crud.db_crud = service
    try:
        yield service
    finally:
        crud.db_crud = original_db


def test_root_endpoint_returns_api_info(web_db_service):
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == 200
    body = response.json()
    assert body['message']
    assert 'docs' in body


def test_list_tables_returns_personas_table(web_db_service):
    client = TestClient(app)
    response = client.get('/api/tables')

    assert response.status_code == 200
    payload = response.json()
    assert 'tables' in payload
    assert 'personas' in payload['tables']


def test_insert_record_calculates_age_from_fecha_nacimiento(web_db_service):
    client = TestClient(app)
    payload = {
        'primer_nombres': 'Sofía',
        'primer_apellido': 'Ramírez',
        'documento': 'CC',
        'numero_identificacion': '2000001',
        'direccion': 'Cra 8 # 10-11',
        'fecha_nacimiento': '2002-03-15',
        'sexo': 'F'
    }

    response = client.post('/api/table/personas/insert', json=payload)
    assert response.status_code == 200, response.text
    result = response.json()
    assert result['success'] is True
    assert result['id'] is not None

    record = client.get(f"/api/table/personas/{result['id']}").json()
    assert record['edad'] >= 0
    assert record['edad'] == 24 or record['edad'] == 23


def test_update_record_changes_name_and_recalculates_age(web_db_service):
    client = TestClient(app)
    initial_payload = {
        'primer_nombres': 'Miguel',
        'primer_apellido': 'Torres',
        'documento': 'TI',
        'numero_identificacion': '2000002',
        'direccion': 'Calle 50',
        'fecha_nacimiento': '1998-12-30',
        'sexo': 'M'
    }

    created = client.post('/api/table/personas/insert', json=initial_payload)
    record_id = created.json()['id']

    update_payload = {
        'primer_nombres': 'Miguel Ángel',
        'fecha_nacimiento': '1998-12-30'
    }
    response = client.put(f'/api/table/personas/{record_id}', json=update_payload)

    assert response.status_code == 200, response.text
    updated = client.get(f'/api/table/personas/{record_id}').json()
    assert updated['primer_nombres'] == 'Miguel Ángel'
    assert updated['edad'] is not None


def test_empty_payload_returns_400(web_db_service):
    client = TestClient(app)
    response = client.post('/api/table/personas/insert', json={})

    assert response.status_code == 400
    assert 'No se recibieron datos' in response.json()['detail']


def test_delete_record_removes_it(web_db_service):
    client = TestClient(app)
    payload = {
        'primer_nombres': 'Laura',
        'primer_apellido': 'Castro',
        'documento': 'CE',
        'numero_identificacion': '2000003',
        'direccion': 'Avenida 9',
        'fecha_nacimiento': '1992-06-01',
        'sexo': 'F'
    }

    created = client.post('/api/table/personas/insert', json=payload)
    record_id = created.json()['id']

    delete_response = client.delete(f'/api/table/personas/{record_id}')
    assert delete_response.status_code == 200
    assert delete_response.json()['success'] is True

    get_response = client.get(f'/api/table/personas/{record_id}')
    assert get_response.status_code == 404
