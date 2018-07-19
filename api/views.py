from flask import Flask, request, jsonify, make_response
from .models import Request, User
import re
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import datetime
from database import DatabaseConnection
from functools import wraps





app = Flask(__name__)

def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return jsonify({'message': 'Provide token'})
        else:
            try:
                jwt.decode(auth, 'secret', algorithms=['HS256'])
            except Exception as e:
                print(e)
                return jsonify({'message': 'Invalid token'})
        return f(*args, **kwargs)
    return decorated


   

@app.route('/api/v2/auth/register', methods=['POST'])
def register_user():

    user_data = request.get_json()
    name = user_data.get('name')
    email = user_data.get('email')
    username = user_data.get('username')
    password = generate_password_hash(user_data.get('password'))
    # password = user_data.get('password')
    is_admin = user_data.get('is_admin')

    if user_data:
        print(user_data)
    if not user_data:
        return jsonify({'message': 'All fields are required'}), 400

    if not name or name == " ":
        return jsonify({'message': 'Invalid name'}), 400

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        return make_response(jsonify({
            "status": "Fail",
            "message": "Enter valid email"}), 400)

    if not username or username == " " or username == type(int):
        return jsonify({'message': 'Invalid username'}), 400

    if not password or password == " " or len(password) < 5:
        return jsonify({'message': 'A stronger password  is required'}), 400

    new_user = User(name, email, username, password, is_admin)
    new_user.add_user()

    return jsonify({"message": f"User {name} successfully created an account"}), 201


@app.route('/auth/login', methods=['POST'])
def login_user():
    user_data = request.get_json()
    # current_user = User(user_data['username'],user_data['password'])
   