from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import init_db
from controllers import auth_bp
from controllers import episode_bp
from controllers import guest_bp
from controllers import appearance_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    init_db(app)
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(appearance_bp)

    @app.route('/')
    def index():
        return {'message': 'Late Show API is running!'}

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)