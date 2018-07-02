
from flask import Flask, request, jsonify
from .models import Request, requests, User, users
import datetime

app = Flask(__name__)


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


@app.route('/users')
def get_all_users():
    return jsonify({'users': users}), 200

@app.route('/users/<int:user_id>')
def get_user(user_id):
    for each_user in users:
        if each_user.get('id') == user_id:
            return jsonify({'user': each_user})
    
    return jsonify({'error':'User Not Found'}), 404


@app.route('/api/v1/users/requests', methods=['POST'])
def create_request():
    # getting request data
    request_data = request.get_json()

    if not request_data:
        return jsonify({'message': 'All fields are required'}), 400
    client_name = request_data.get('client_name')
    email = request_data.get('email')
    category = request_data.get('category')
    request_title = request_data.get('request_title')
    description = request_data.get('description')
    department = request_data.get('department')
    # request_time = datetime.datetime.now()

    # validate request data
    if not client_name:
        return jsonify({'message': 'client name is required'}), 400

    if not email:
        return jsonify({'message': 'Email address is required'}), 400     

    if not category:
        return jsonify({'message': 'category is required'}), 400 
    if not request_title:
        return jsonify({'message': 'request title  is required'}), 400 

    if not description:
        return jsonify({'message': 'Description is required'}), 400 

    if not department:
        return jsonify({'message': 'datetime is required'}), 400 

                     

    request_data['id'] = len(requests)
    requests.append(request_data)

    return jsonify({ 'message': f'Hey {client_name}! You have successfully created a request'}), 201



@app.route('/api/v1/users/requests', methods=['GET'])
def get_all_requests():
    if len(requests) > 0:
       return jsonify({"message": requests}),302
    else:
        return jsonify({"message":"There are no requests found"}),404 
       

@app.route('/api/v1/users/requests/<int:request_id>', methods=['GET'])
def get_single_request(request_id):
    for single_request in requests:
        if single_request.get('id') == request_id:
            return jsonify({'request': single_request})
    
    return jsonify({'message':'That request is Not Found'}), 404

@app.route('/api/v1/users/requests/<int:request_id>', methods=['PUT'])
def modify_request(request_id):
    pass
    