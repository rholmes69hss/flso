from flask import jsonify
from app import app
from app.models import User, Post
from app.utils import serialize_user

@app.route('/api/users', methods=['GET'])
def user_index2():
    users = User.query.all()
    return jsonify([ 
        serialize_user(user)
        for user in users
    ])
