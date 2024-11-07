from flask import Flask
from app_flask import Config
from models import db
from routes import usuario_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(usuario_bp)

    with app.app_context():
        db.create_all()

    return app
