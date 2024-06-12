import json
import pytest
from unittest.mock import patch
from app import app
from controllers.employees_controller import CustomException

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_employees(client):
    response = client.get('/employees')
    assert response.status_code == 200
    assert 'employees' in response.json

def test_get_employee(client):
    response = client.get('/employees/1')
    if response.status_code == 200:
        assert 'id' in response.json
        assert response.json['id'] == 1
    else:
        assert response.status_code == 404
        assert 'error' in response.json

def test_create_employee(client):
    new_employee = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "role": "Keeper",
        "schedule": "Mon-Fri"
    }
    response = client.post('/employees', data=json.dumps(new_employee), content_type='application/json')
    if response.status_code == 201:
        assert 'message' in response.json
        assert response.json['message'] == "Successfully created a new employee"
    else:
        assert response.status_code == 400
        assert 'message' in response.json

def test_update_employee(client):
    updated_employee = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "0987654321",
        "role": "Manager",
        "schedule": "Mon-Fri"
    }
    response = client.put('/employees/1', data=json.dumps(updated_employee), content_type='application/json')
    if response.status_code == 200:
        assert 'message' in response.json
        assert response.json['message'] == "Employee updated successfully"
    elif response.status_code == 404:
        assert 'error' in response.json
        assert response.json['error'] == "Employee not found"
    else:
        assert response.status_code == 400
        assert 'message' in response.json

def test_delete_employee(client):
    response = client.delete('/employees/1')
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == "Employee deleted successfully"

@patch('controllers.employees_controller.validate_employee_data')
def test_mock(mocked_validate_employee_data, client):
    mocked_validate_employee_data.return_value = None
    side_effect = CustomException("Jiakh", 403)
    mocked_validate_employee_data.side_effect = side_effect
    response = client.post('/employees', json={'name': 'john doe'})
    assert response.status_code == 403
    assert response.json == {"message": "Jiakh"}
