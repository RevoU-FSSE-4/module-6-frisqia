from flask import Flask, jsonify, request
from db import zoo, animal

app = Flask(__name__)

# Route to man page
@app.route('/Home', methods=['GET'])
def dashboard():
    return "Welcome in the zoo"

# Route to get data zoo
@app.route('/zoo', methods=['GET'])
def get_zoo():
    return jsonify({"zoo": zoo})

# Route to get all animal
@app.route('/animals', methods=['GET'])
def get_animals():
    return jsonify({"animals": animal})

# Route to get animal data by ID
@app.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    animal_found = next((a for a in animal if a['id'] == id), None)
    if animal_found:
        return jsonify(animal_found)
    else:
        return jsonify({"error": "Animal not found"}), 404

# route to create animal data
@app.route('/animals', methods=['POST'])
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

# Route to renew animal data
@app.route('/animals/<int:id>', methods=['PUT'])
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

# Route to delete animal data
@app.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    global animal
    animal = [a for a in animal if a['id'] != id]
    return jsonify({"message": "Animal deleted successfully"}), 200

# function to validate new animal data
def validate_animal_data(data):
    required_fields = ['name', 'species', 'food', 'origin']
    for field in required_fields:
        if field not in data or not data[field]:
            raise Exception(f"Please ensure you provide {field} for the animal")

if __name__ == '__main__':
    app.run(debug=True, port=5000)

