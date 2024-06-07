from flask import Blueprint
from controllers.animals_controller import get_zoo, get_animals, get_animal, create_animal, update_animal, delete_animal

animals_bp = Blueprint('animals', __name__)

animals_bp.route('/zoo', methods=['GET'])(get_zoo)
animals_bp.route('/animals', methods=['GET'])(get_animals)
animals_bp.route('/animals/<int:id>', methods=['GET'])(get_animal)
animals_bp.route('/animals', methods=['POST'])(create_animal)
animals_bp.route('/animals/<int:id>', methods=['PUT'])(update_animal)
animals_bp.route('/animals/<int:id>', methods=['DELETE'])(delete_animal)
