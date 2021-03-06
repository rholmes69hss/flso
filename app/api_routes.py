from flask import jsonify
from app import app
from app.models import User, Post, Role
from app.utils import serialize_user, serialize_role

@app.route('/api/users', methods=['GET'])
def user_index2():
    users = User.query.all()
    return jsonify([ 
        serialize_user(user)
        for user in users
    ])

@app.route('/api/roles', methods=['GET'])
def getroles():
    roles = Role.query.all()
    return jsonify([ 
        serialize_role(role)
        for role in roles
    ])