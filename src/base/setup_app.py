from flask import Flask

from src.routes.health import app as health


def _setup_db():
    pass


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(health)
    return app
