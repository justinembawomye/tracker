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


@app.route('/api/v2/auth/login', methods=['POST'])
def login_user():
    connect = DatabaseConnection()
    cursor = connect.cursor
    login_data = request.get_json()
    username = login_data['username']
    password = generate_password_hash(login_data['password'])
  
    cursor.execute(
        "SELECT * FROM users WHERE username = '{}'".format(login_data['username']))
    user = cursor.fetchone()

    if user:

        user_object = User(user[1], user[2], user[3], user[4])

        user_token = user_object.get_token()
        return jsonify({
            'status': 'OK',
            'message': f'Welcome {username} You are logged in',
            'access_token': user_token.decode('utf8')
            }), 200
    else:
        return jsonify({
            'message': f'user {username} not found'
        }), 404

   
@app.route('/api/v2/users/requests', methods=['POST'])
def create_request():

    request_data = request.get_json()
    client_name = request_data.get('client_name')
    email = request_data.get('email')
    category = request_data.get('category')
    request_title = request_data.get('request_title')
    description = request_data.get('description')
    department = request_data.get('department')
    status = request_data.get('status')

    if request_data:
        print(request_data)
    if not request_data:
        return jsonify({'message': 'All fields are missing'}), 400

    if not client_name or client_name == " ":
        return jsonify({'message': 'name field is missing'}), 400

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        return make_response(jsonify({
            "status": "Fail",
            "message": "Enter a valid email"}), 400)

    if not category or category == " ":
        return jsonify({'message':'category field is missing'}), 400
    if not request_title or request_title == " ":
        return jsonify({'message':'request_title is missing'}), 400
    if not description or description == " ":
        return jsonify({'message':'description field is missing'}), 400
    if not department or department == " ":
        return jsonify({'message':'department field is missing'}), 400



    new_request = Request(client_name, email, category, request_title, description, department, status)
    new_request.create_request()

    return jsonify({"message": f"User {client_name} successfully created a request"}), 201

   