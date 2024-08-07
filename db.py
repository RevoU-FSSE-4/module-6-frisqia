import json

# read file employees.json and save to variabel employees
with open('employees.json', 'r') as file:
    employees = json.load(file)

zoo = [
    {
        "id": 1,
        "species": "Mamalia",
        "special_requirements": "Use Iron cage"
    },
    {
        "id": 2,
        "species": "Aves",
        "special_requirements": "Using Glass enclosure"
    },
    {
        "id": 3,
        "species": "Reptil",
        "special_requirements": "Using Glass and Iron enclosures"
    },
]

animal = [
    {
        "id": 1,
        "name": "Lion",
        "zoo_id": 1,
        "food": "Karnivora",
        "origin": "Benua Afrika",
    },
    {
        "id": 2,
        "name": "Cendrawasih",
        "zoo_id": 2,
        "food": "Herbivora",
        "origin": "Jayapura",
    },
    {
        "id": 3,
        "name": "Estuarine Crocodile",
        "zoo_id": 3,
        "food": "Karnivora",
        "origin": "Australia",
    },
    {
        "id": 4,
        "name": "Comodo",
        "zoo_id": 3,
        "food": "Karnivora",
        "origin": "Nusa Tenggara Timur, Indonesia",
    },
    {
        "id": 5,
        "name": "Pelican",
        "zoo_id": 2,
        "food": "Karnivora",
        "origin": "Amerika Selatan",
    },
    {
        "id": 6,
        "name": "hippopotamus",
        "zoo_id": 2,
        "food": "omnivora",
        "origin": "Afrika sub-Sahara",
    },
    {
        "id": 7,
        "name": "Gorila",
        "zoo_id": 1,
        "food": "herbivora",
        "origin": "Afrika",
    },
]
