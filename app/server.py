from flask import Flask

from app.views import start_bp, fight_bp


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    app.register_blueprint(start_bp)
    app.register_blueprint(fight_bp)

    return app
