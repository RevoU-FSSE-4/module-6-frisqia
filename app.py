from flask import Flask, jsonify, request
from db import zoo, animal

app = Flask(__name__)

@app.route('/Home', methods=['GET', 'POST'])
def dashboard():
    return "Welcome in the zoo"

@app.get('/zoo')
def get_zoo():
    return jsonify({"inzoo": zoo})

@app.get('/animal')
def get_animal():
    return jsonify({"animal": animal})

@app.post('/animal')
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
            return jsonify({"error": "species animal is not found"}), 400
        
        new_id = len(animal) + 1
        new_animal = {
            "id": new_id,
            "name": data['name'],
            "zoo_id": zoo_id,
            "food": data['food'],
            "origin": data['origin']
        }
        animal.append(new_animal)
        return jsonify({"message": "successfully created a new animal"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

def validate_animal_data(data):
    required_fields = ['name', 'species', 'food', 'origin']
    for field in required_fields:
        if field not in data or not data[field]:
            raise Exception(f"Please ensure you provide {field} for the animal")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
