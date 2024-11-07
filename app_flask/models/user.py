from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'
