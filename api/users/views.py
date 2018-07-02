
from api import app
from flask import request, jsonify
from .models import User, users



@app.route('/auth/register', methods=['POST'])
def register_user():
    # getting user data
    user_data = request.get_json()

    if not user_data:
        return jsonify({'message': 'All fields are required'}), 400
    name = user_data.get('name')
    email = user_data.get('email')
    username = str(user_data.get('username')).strip()
    password = user_data.get('password')

    # validate user data
    if not name:
        return jsonify({'message': 'name is required'}), 400

    if not email:
        return jsonify({'message': 'Email address is required'}), 400     

    if not username:
        return jsonify({'message': 'username is required'}), 400 

    user_data['id'] = len(users)
    # Add users
    users.append(user_data)

    return jsonify({ 'message': f'User {username} has been registered'}), 201


@app.route('/auth/login', methods=['POST'])
def login_user():
    # getting user data
    user_data = request.get_json()

    if not user_data:
        return jsonify({'Missing': 'These fields are required'}), 400
    username = str(user_data.get('username')).strip()
    password = user_data.get('password')

    # validate user data
    if not username:
        return jsonify({'message': 'username is required'}), 400 

    if not password:
        return jsonify({'message': 'password missing! This field is required'}), 400     
    return jsonify({ 'message': f'Welcome {username} You are logged in'}), 200


@app.route('/users')
def get_all_users():
    return jsonify({'users': users}), 200

@app.route('/users/<int:user_id>')
def get_user(user_id):
    for each_user in users:
        if each_user.get('id') == user_id:
            return jsonify({'user': each_user})
    
    return jsonify({'error':'User Not Found'}), 404