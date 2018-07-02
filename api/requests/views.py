
from api import app
from flask import request, jsonify
from .models import Request, requests
import datetime



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