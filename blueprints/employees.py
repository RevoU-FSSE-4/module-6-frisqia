from flask import Blueprint
from controllers.employees_controller import get_employees, get_employee, create_employee, update_employee, delete_employee

employees_bp = Blueprint('employees', __name__)

employees_bp.route('/employees', methods=['GET'])(get_employees)
employees_bp.route('/employees/<int:id>', methods=['GET'])(get_employee)
employees_bp.route('/employees', methods=['POST'])(create_employee)
employees_bp.route('/employees/<int:id>', methods=['PUT'])(update_employee)
employees_bp.route('/employees/<int:id>', methods=['DELETE'])(delete_employee)
