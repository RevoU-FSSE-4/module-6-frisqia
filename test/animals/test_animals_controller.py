import json
import pytest
from unittest.mock import patch
from app import app
from controllers.animals_controller import CustomException

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_zoo(client):
    response = client.get('/zoo')
    assert response.status_code == 200
    assert 'zoo' in response.json

def test_get_animals(client):
    response = client.get('/animals')
    assert response.status_code == 200
    assert 'animals' in response.json

def test_get_animal(client):
    response = client.get('/animals/1')
    if response.status_code == 200:
        assert 'id' in response.json
        assert response.json['id'] == 1
    else:
        assert response.status_code == 404
        assert 'error' in response.json

def test_create_animal(client):
    new_animal = {
        "name": "Lion",
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.post('/animals', data=json.dumps(new_animal), content_type='application/json')
    if response.status_code == 201:
        assert 'message' in response.json
        assert response.json['message'] == "Successfully created a new animal"
    else:
        assert response.status_code == 400
        assert 'message' in response.json

def test_update_animal(client):
    updated_animal = {
        "name": "Lioness",
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.put('/animals/1', data=json.dumps(updated_animal), content_type='application/json')
    if response.status_code == 200:
        assert 'message' in response.json
        assert response.json['message'] == "Animal updated successfully"
    elif response.status_code == 404:
        assert 'error' in response.json
        assert response.json['error'] == "Animal not found"
    else:
        assert response.status_code == 400
        assert 'message' in response.json

def test_delete_animal(client):
    response = client.delete('/animals/1')
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == "Animal deleted successfully"

@patch('controllers.animals_controller.validate_animal_data')
def test_mock(mocked_validate_animal_data, client):
    mocked_validate_animal_data.return_value = None
    side_effect = CustomException("Jiakh", 403)
    mocked_validate_animal_data.side_effect = side_effect
    response = client.post('/animals', json={'name': 'john doe'})
    assert response.status_code == 403
    assert response.json == {"message": "Jiakh"}
