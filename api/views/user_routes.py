from flask import Flask, request, jsonify, abort
import json
#from application import app
from api.models import User, Request

app = Flask(__name__)

all_requests = []
users = []

@app.route("/user/register", methods=["POST"])
def register():
    """Endpoint to register a new user"""
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    if not name:
        return jsonify({"message": "Missing name missing"}), 400

    if not email:
        return jsonify({"message": "Email address missing"}), 400
    if not username:
        return jsonify({"message": "username is missing"}), 400
    if not password:
        return jsonify({"message": "password missing.Please Enter a password"}), 400
   
    new_user = User(name, email, username, password)
    users.append(new_user)
    return jsonify({'message':'successfully registered a new user'}), 201
