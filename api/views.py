from flask import Flask, request, jsonify
from .models import Request, requests, User, users
import datetime


app = Flask(__name__)


@app.route('/auth/register', methods=['POST'])
def register_user():
    user_data = request.get_json()
    # getting user data
    name = user_data.get('name')
    email = user_data.get('email')
    username = str(user_data.get('username')).strip()
    password = user_data.get('password')

    if not user_data:
        return jsonify({'message': 'All fields are required'}), 400

    if not name or name == " " or name == type(int) or len(name) < 3:
        return jsonify({'message': 'Invalid name'}), 400

    if not email or email == " ":
        return jsonify({'message': 'Email address is missing'}), 400

    if not username or username == " " or username == type(int):
        return jsonify({'message': 'Invalid username'}), 400
    if not password or password == " " or len(password) < 5:
        return jsonify({'message': 'A stronger password  is required'}), 400

    user_data['id'] = len(users)
    # Add users
    users.append(user_data)

    return jsonify({'message': f'User {username} has been registered'}), 201


@app.route('/auth/login', methods=['POST'])
def login_user():
    # getting user data
    user_data = request.get_json()

    if not user_data:
        return jsonify({'Missing': 'These fields are required'}), 400
    username = str(user_data.get('username')).strip()
    password = user_data.get('password')

    return jsonify({"message":"Welcome Tinah. You are logged in"})


@app.route('/users')
def get_all_users():
    return jsonify({'users': users}), 200


@app.route('/users/<int:user_id>')
def get_user(user_id):
    for each_user in users:
        if each_user.get('id') == user_id:
            return jsonify({'user': each_user})

    return jsonify({'error': 'User Not Found'}), 404


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
    if not client_name or client_name == " " or len(client_name < 3) or client_name == type(int):
        return jsonify({'message': 'client name is required'}), 400

    if not email or email == " ":
        return jsonify({'message': 'Email address is required'}), 400

    if not category or category == " ":
        return jsonify({'message': 'category is required'}), 400
    if not request_title or request_title == "":
        return jsonify({
            'status': 'Required',
            'message': 'request title field is missing'}), 400

<<<<<<< HEAD
    if not description or description == " " or len(description < 10):
        return jsonify({'message': 'Description is required'}), 400
=======
    if not department:
        return jsonify({'message': 'department is required'}), 400 
>>>>>>> challenge2

    if not department or department == " ":
        return jsonify({
            'status': 'Fail',
            'message': 'department field  is missing'}), 400

    request_data['id'] = 0
    request_data['id'] = len(requests)
    requests.append(request_data)

    return jsonify({'message': f'Hey {client_name}! You have successfully created a request'}), 201


@app.route('/api/v1/users/requests', methods=['GET'])
def get_all_requests():
    if len(requests) > 0:
        return jsonify({"message": requests}), 302
    else:
        return jsonify({
            "status": "Fail",
            "message": "There are no requests found on the system"}), 404


@app.route('/api/v1/users/requests/<int:request_id>', methods=['GET'])
def get_single_request(request_id):
    """ Endpoint to fetch a single request """

    for single_request in requests:
        if single_request.get('id') == request_id:
            return jsonify({'request': single_request})

    return jsonify({
        'status': 'Fail',
        'message': 'That request is doesn\'t exist'}), 404


@app.route("/api/v1/users/requests/<int:requestId>", methods=['PUT'])
def update_request(request_id):
    """ Endpoint to edit a user request"""

    # check if user has any requests
    if len(requests) < 0:
        return jsonify({
            "status": "Not found",
            "message": "You haven't made any requests"
        }), 400

    # if user has more than one request
    if len(requests) >= 1:
        # get entered data
        data = request.get_json()

        # picking the request attributes
        client_name = data.get("client_name")
        email = data.get("email")

        if len(requests) >= 1:
            for single_request in requests:
                if single_request.request_id == int(request_id):
                    single_request.client_name = client_name
                    single_request.email = email
                    single_request.category = category
                    single_request.request_title = request_title
                    single_request.department = department
                    single_request.description = description
                    return jsonify({
                        "message": "Successfully edited the request"
                    })
