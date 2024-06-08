from flask import jsonify, request
from db import employees

def get_employees():
    """
    Get list of employees
    ---
    responses:
      200:
        description: A list of employees
    """
    return jsonify({"employees": employees})

def get_employee(id):
    """
    Get an employee by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the employee
    responses:
      200:
        description: An employee
      404:
        description: Employee not found
    """
    employee = next((e for e in employees if e['id'] == id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

def create_employee():
    """
    Create a new employee
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
            phone:
              type: string
            role:
              type: string
            schedule:
              type: string
    responses:
      201:
        description: Successfully created a new employee
      400:
        description: Invalid input
    """
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

def update_employee(id):
    """
    Update an employee by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the employee
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
            phone:
              type: string
            role:
              type: string
            schedule:
              type: string
    responses:
      200:
        description: Employee updated successfully
      400:
        description: Invalid input
      404:
        description: Employee not found
    """
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

def delete_employee(id):
    """
    Delete an employee by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the employee
    responses:
      200:
        description: Employee deleted successfully
    """
    global employees
    employees = [e for e in employees if e['id'] != id]
    return jsonify({"message": "Employee deleted successfully"}), 200

def validate_employee_data(data):
    required_fields = ['name', 'email', 'phone', 'role', 'schedule']
    for field in required_fields:
        if field not in data or not data[field]:
            raise Exception(f"Please ensure you provide {field} for the employee")
