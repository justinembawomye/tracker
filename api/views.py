from flask import Flask, request, jsonify, make_response
from .models import Request, requests, User, users
import re

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

    
    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        return make_response(jsonify({
            "status":"Fail",
            "message": "Enter valid email"}), 400)

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
    username = str(user_data.get('username')).strip()
    password = user_data.get('password')

    if not user_data:
        return jsonify({'Missing': 'These fields are required'}), 400

    if not username or username ==" ":
        return jsonify({'Missing': 'username is required'}), 400
        
    if not password or password ==" ":
        return jsonify({'Missing': 'password  is required'}), 400    
    return jsonify({"message": f"Welcome {username}. You are logged in"})

    return jsonify({"message": f"Welcome {username}. You are logged in"}),200



@app.route("/api/v1/users/requests", methods=["POST"])
def create_request():
    """ Endpoint to get the request data entered by the user """
    #get request data
    request_data = request.get_json()

   
    client_name = request_data.get("client_name")
    email = request_data.get("email")
    category  = request_data.get("category")
    request_title = request_data.get("request_title")
    description = request_data.get("description")
    department = request_data.get("department")
    request_id = len(requests) + 1
    

 # validate request data
    
    if not client_name or client_name == " " or client_name == type(int):
        return jsonify({'message': 'client name is required'}), 400   

       
    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        return make_response(jsonify({
            "status":"Fail",
            "message": "Enter valid email"}), 400)
    if not category or category == " ":
        return jsonify({'message': 'category is required'}), 400
    if not request_title or request_title == "":
        return jsonify({
            'status': 'Required',
            'message': 'request title field is missing'}), 400

    if not description or description == " ":
        return jsonify({'message': 'Description is missing'}), 400

    if not department or department == " ":
        return jsonify({
            'status': 'Fail',
            'message': 'department field  is missing'}), 400

    new_request = Request(client_name, email, category, request_title, description, department, request_id)
    requests.append(new_request)


    return jsonify({'message': f'Hey {client_name}! You have successfully created a request'}), 201



@app.route("/api/v1/users/requests", methods=["GET"])
def fetch_requests():
    if len(requests) < 1:
        return jsonify({
            "message":"You have no requests"
        }), 400
    
    if len(requests) >= 1:
        return jsonify({
            "message":requests
        }),302
    return jsonify({"message":"Can\'t fetch requests "}),400

@app.route('/api/v1/users/requests/<int:request_id>', methods=['GET'])
def get_single_request(request_id):
    """ Endpoint to fetch a single request """

    for single_request in requests:
        if single_request.get('id') == request_id:
            return jsonify({'request': single_request})

    return jsonify({
        'status': 'Fail',
        'message': 'That request is doesn\'t exist'}), 404


@app.route("/api/v1/users/requests/<int:request_id>", methods=['PUT'])
def update_request(request_id):
    """ Endpoint to edit a request"""
    new_request_data = request.get_json()
    for i in requests:
        if i:
            client_name = new_request_data.get('client_name')
            email = new_request_data.get('email')
            category = new_request_data.get('category')
            request_title = new_request_data.get('request_title')
            description = new_request_data.get('description')
            department = new_request_data.get('department')
        return jsonify({"message":"Request updated successfully"}),200 


    return jsonify({"message":"Failed to update request"}),400

