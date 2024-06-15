import json
import pytest
from unittest.mock import patch
from controllers.animals_controller import CustomException

def test_custom_exception():
    with pytest.raises(CustomException):
        raise CustomException("This is a custom exception")

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


def test_get_animal_not_found(client):
    response = client.get('/animals/999')  
    assert response.status_code == 404
    assert 'error' in response.json
    assert response.json['error'] == "Animal not found"

def test_create_animal_missing_name(client):
    new_animal = {
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.post('/animals', data=json.dumps(new_animal), content_type='application/json')
    assert response.status_code == 400
    assert 'message' in response.json

def test_update_animal_not_found(client):
    updated_animal = {
        "name": "Lioness",
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.put('/animals/999', data=json.dumps(updated_animal), content_type='application/json')  # ID yang tidak ada
    assert response.status_code == 404
    assert 'error' in response.json
    assert response.json['error'] == "Animal not found"

def test_update_animal_invalid_data(client):
    updated_animal = {
        "name": "", 
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.put('/animals/1', json=updated_animal)
    assert response.status_code == 404
    assert 'error' in response.json
    assert response.json['error'] == "Animal not found"

def test_delete_animal_not_found(client):
    response = client.delete('/animals/999')  
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == "Animal deleted successfully"

@patch('controllers.animals_controller.validate_animal_data')
def test_mock(mocked_validate_animal_data, client):
    side_effect = CustomException("Jiakh")
    mocked_validate_animal_data.side_effect = side_effect
    response = client.post('/animals', json={'name': 'john doe'})
    assert response.status_code == 400
    assert response.json == {"message": "Jiakh"}

def test_create_animal_empty_name(client):
    new_animal = {
        "name": "",
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.post('/animals', json=new_animal)
    assert response.status_code == 400
    assert 'message' in response.json

def test_create_animal_species_not_found(client):
    new_animal = {
        "name": "Giraffe",
        "species": "Giraffa camelopardalis",
        "food": "Leaves",
        "origin": "Africa"
    }
    response = client.post('/animals', json=new_animal)
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == "Species animal is not found"

def test_update_animal_no_changes(client):
    updated_animal = {
        "name": "Lion",
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.put('/animals/1', json=updated_animal)
    assert response.status_code == 404 


def test_update_animal_not_allowed_fields(client):
    updated_animal = {
        "id": 1,
        "name": "Lion",
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.put('/animals/1', json=updated_animal)
    assert response.status_code == 404  

@patch('controllers.animals_controller.validate_animal_data')
def test_validate_animal_data_exception(mock_validate_animal_data, client):
    mock_validate_animal_data.side_effect = CustomException("Custom validation error")
    new_animal = {
        "name": "Tiger",
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Asia"
    }
    response = client.post('/animals', json=new_animal)
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == "Custom validation error"

def test_create_animal_empty_data(client):
    response = client.post('/animals', json={})
    assert response.status_code == 400
    assert 'message' in response.json

def test_create_animal_invalid_data_types(client):
    new_animal = {
        "name": "Lion",
        "species": 123,  
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.post('/animals', json=new_animal)
    assert response.status_code == 400
    assert 'message' in response.json

def test_create_animal_missing_fields(client):
    new_animal = {
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.post('/animals', json=new_animal)
    assert response.status_code == 400
    assert 'message' in response.json

def test_update_animal_non_existent(client):
    updated_animal = {
        "name": "panda",
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.put('/animals/999', json=updated_animal)
    assert response.status_code == 404
    assert 'error' in response.json

def test_update_animal_modify_id(client):
    updated_animal = {
        "id": 2,  
        "name": "Lioness",
        "species": "Mamalia",
        "food": "Meat",
        "origin": "Africa"
    }
    response = client.put('/animals/1', json=updated_animal)
    assert response.status_code == 404
    assert 'error' in response.json
    assert response.json['error'] == "Animal not found"

