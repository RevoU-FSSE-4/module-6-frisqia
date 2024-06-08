from flask import jsonify, request
from db import zoo, animal

def get_zoo():
    """
    Get list of zoos
    ---
    responses:
      200:
        description: A list of zoos
    """
    return jsonify({"zoo": zoo})

def get_animals():
    """
    Get list of animals
    ---
    responses:
      200:
        description: A list of animals
    """
    return jsonify({"animals": animal})

def get_animal(id):
    """
    Get an animal by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the animal
    responses:
      200:
        description: An animal
      404:
        description: Animal not found
    """
    animal_found = next((a for a in animal if a['id'] == id), None)
    if animal_found:
        return jsonify(animal_found)
    else:
        return jsonify({"error": "Animal not found"}), 404

def create_animal():
    """
    Create a new animal
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
            species:
              type: string
            food:
              type: string
            origin:
              type: string
    responses:
      201:
        description: Successfully created a new animal
      400:
        description: Invalid input
    """
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

def update_animal(id):
    """
    Update an animal by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the animal
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            species:
              type: string
            food:
              type: string
            origin:
              type: string
    responses:
      200:
        description: Animal updated successfully
      400:
        description: Invalid input
      404:
        description: Animal not found
    """
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

def delete_animal(id):
    """
    Delete an animal by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the animal
    responses:
      200:
        description: Animal deleted successfully
    """
    global animal
    animal = [a for a in animal if a['id'] != id]
    return jsonify({"message": "Animal deleted successfully"}), 200

def validate_animal_data(data):
    required_fields = ['name', 'species', 'food', 'origin']
    for field in required_fields:
        if field not in data or not data[field]:
            raise Exception(f"Please ensure you provide {field} for the animal")
