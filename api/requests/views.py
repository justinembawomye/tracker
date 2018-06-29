from flask import request
from api import app

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return 'Hello World!'
    
    if request.method == 'GET':
        return 'We are using get'