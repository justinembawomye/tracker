
from api import app
from flask import request, jsonify

users = []

@app.route('/auth/register', methods=['POST'])
def register_user():
    # getting user data
    user_data = request.get_json()

    if not user_data:
        return jsonify({'message': 'All fields are required'}), 400

    email = user_data.get('email')
    password = user_data.get('password')
    username = str(user_data.get('username')).strip()

    # validate user data
    if not username:
        return jsonify({'message': 'Username is required'}), 400
    
    user_data['id'] = len(users)
    # store your data to your database
    users.append(user_data)

    return jsonify({ 'message': f'User {username} has been registered'}), 201

@app.route('/users')
def get_all_users():
    return jsonify({'users': users}), 200

@app.route('/users/<int:user_id>')
def get_user(user_id):
    for each_user in users:
        if each_user.get('id') == user_id:
            return jsonify({'user': each_user})
    
    return jsonify({'error':'User Not Found'}), 404