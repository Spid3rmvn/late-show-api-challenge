from flask import Flask
from flask import Flask
from flask_jwt_extended import JWTManager
from server.config import Config
from server.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db(app)
    jwt = JWTManager(app)

    @app.route('/')
    def index():
        return {'message': 'Late Show API is running!'}

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)