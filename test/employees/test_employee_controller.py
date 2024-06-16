def test_get_employees(client):
    response = client.get('/employees')
    assert response.status_code == 200
    assert isinstance(response.json, dict)  # Ensure response.json is a dictionary
    assert "employees" in response.json

def test_create_employee(client):
    new_employee = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "1234567890",
        "role": "Keeper",
        "schedule": "Mon-Fri"
    }
    response = client.post('/employees', json=new_employee)
    assert response.status_code == 201
    assert "message" in response.json

def test_get_employee_by_id(client):
    employee_id = 1  # Ensure this ID exists in your database
    response = client.get(f'/employees/{employee_id}')
    assert response.status_code == 200
    assert isinstance(response.json, dict)

def test_update_employee(client):
    employee_id = 1  # Ensure this ID exists in your database
    updated_data = {
        "name": "Updated Employee",
        "email": "updatedemail@example.com",
        "phone": "0987654321",
        "role": "Manager",
        "schedule": "Mon-Fri"
    }
    response = client.put(f'/employees/{employee_id}', json=updated_data)
    assert response.status_code == 200
    assert "message" in response.json

def test_delete_employee(client):
    employee_id = 1  # Ensure this ID exists in your database
    response = client.delete(f'/employees/{employee_id}')
    assert response.status_code == 200
    assert "message" in response.json