from flask import jsonify, request
import os
import sys
from db import employees
from flasgger import swag_from
current_dir = os.path.dirname(os.path.abspath(__file__))
# # parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

class CustomException(Exception):
    code = 403
    description = "Forbidden"

def validate_employees_data(data):
    if not data.get('name'):
        raise CustomException("Employees name is required")
    return True


@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'get_employees.yml'))
def get_employees():
    return jsonify({"employees": employees})

@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'get_employees_byID.yml'))
def get_employee(id):
    employee = next((e for e in employees if e['id'] == id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'create_employees.yml'))
def create_employee():
    try:
        data = request.get_json()
        validate_employee_data(data)

        new_id = len(employees) + 1
        new_employee = {
            "id": new_id,
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "role": data['role'],
            "schedule": data['schedule']
        }
        employees.append(new_employee)
        return jsonify({"message": "Successfully created a new employee"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'update_employees.yml'))
def update_employee(id):
    try:
        data = request.get_json()
        employee_to_update = next((e for e in employees if e['id'] == id), None)
        if employee_to_update:
            validate_employee_data(data)
            employee_to_update.update(data)
            return jsonify({"message": "Employee updated successfully"}), 200
        else:
            return jsonify({"error": "Employee not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'delete_employees.yml'))
def delete_employee(id):
    global employees
    employees = [e for e in employees if e['id'] != id]
    return jsonify({"message": "Employee deleted successfully"}), 200

def validate_employee_data(data):
    required_fields = ['name', 'email', 'phone', 'role', 'schedule']
    for field in required_fields:
        if field not in data or not data[field]:
            raise Exception(f"Please ensure you provide {field} for the employee")
