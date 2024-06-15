from flask import jsonify, request
from db import zoo, animal
from flasgger import swag_from
import copy
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

class CustomException(Exception):
    code = 403
    description = "Forbidden"

def validate_animal_data(data):
    if not data.get('name'):
        raise CustomException("Animal name is required")
    return True


@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'get_zoo.yml'))
def get_zoo():
    return jsonify({"zoo": zoo}) ,200

@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'get_animals.yml'))
def get_animals():
    return jsonify({"animals": animal}), 200

@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'get_animals_byID.yml'))
def get_animal(id):
    animal_found = next((a for a in animal if a['id'] == id), None)
    if animal_found:
        return jsonify(animal_found)
    else:
        return jsonify({"error": "Animal not found"}), 404

@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'create_animals.yml'))
def create_animal():
    try:
        data = request.get_json()
        validate_animal_data(data)

        zoo_id = None
        for z in zoo:
            if z['species'].lower() == data['species'].lower():
                zoo_id = z['id']
                break

        if zoo_id is None:
            return jsonify({"error": "Species animal is not found"}), 400

        new_id = len(animal) + 1
        new_animal = {
            "id": new_id,
            "name": data['name'],
            "zoo_id": zoo_id,
            "food": data['food'],
            "origin": data['origin']
        }
        animal.append(new_animal)
        return jsonify({"message": "Successfully created a new animal"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'update_animals.yml'))
def update_animal(id):
    try:
        data = request.get_json()
        animal_to_update = next((a for a in animal if a['id'] == id), None)
        if animal_to_update:
            validate_animal_data(data)
            animal_to_update.update(data)
            return jsonify({"message": "Animal updated successfully"}), 200
        else:
            return jsonify({"error": "Animal not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@swag_from(os.path.join(current_dir, '..', 'swagger_doc', 'delete_animals.yml'))
def delete_animal(id):
    global animal
    animal = [a for a in animal if a['id'] != id]
    return jsonify({"message": "Animal deleted successfully"}), 200

def validate_animal_data(data):
    required_fields = ['name', 'species', 'food', 'origin']
    for field in required_fields:
        if field not in data or not data[field]:
            raise Exception(f"Please ensure you provide {field} for the animal")

