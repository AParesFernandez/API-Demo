from flask import Blueprint, request, jsonify
from models import user, db, Usuario

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(nombre=data['nombre'], edad=data['edad'], email=data['email'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'id': nuevo_usuario.id}), 201

@usuario_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id': u.id, 'nombre': u.nombre, 'edad': u.edad, 'email': u.email} for u in usuarios])

@usuario_bp.route('/usuarios/<uuid:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(str(id))
    return jsonify({'id': usuario.id, 'nombre': usuario.nombre, 'edad': usuario.edad, 'email': usuario.email})

@usuario_bp.route('/usuarios/<uuid:id>', methods=['PUT'])
def update_usuario(id):
    data = request.get_json()
    usuario = Usuario.query.get_or_404(str(id))
    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.edad = data.get('edad', usuario.edad)
    usuario.email = data.get('email', usuario.email)
    db.session.commit()
    return jsonify({'id': usuario.id, 'nombre': usuario.nombre, 'edad': usuario.edad, 'email': usuario.email})

@usuario_bp.route('/usuarios/<uuid:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(str(id))
    db.session.delete(usuario)
    db.session.commit()
    return '', 204
