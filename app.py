from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from blueprints.animals import animals_bp
from blueprints.employees import employees_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(animals_bp)
app.register_blueprint(employees_bp)

@app.route('/Home', methods=['GET'])
def dashboard():
    return "Welcome to the zoo"

# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Zoo API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

