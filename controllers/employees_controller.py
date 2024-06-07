from flask import jsonify, request
from db import employees

def get_employees():
    return jsonify({"employees": employees})

def get_employee(id):
    employee = next((e for e in employees if e['id'] == id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

def create_employee():
    try:
        data = request.get_json()
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
        return jsonify({"message": "Employee created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def update_employee(id):
    try:
        data = request.get_json()
        employee = next((e for e in employees if e['id'] == id), None)
        if employee:
            employee.update(data)
            return jsonify({"message": "Employee updated successfully"})
        else:
            return jsonify({"error": "Employee not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def delete_employee(id):
    global employees
    employee = next((e for e in employees if e['id'] == id), None)
    if employee:
        employees = [e for e in employees if e['id'] != id]
        return jsonify({"message": "Employee deleted successfully"})
    else:
        return jsonify({"error": "Employee not found"}), 404
