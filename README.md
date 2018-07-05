# maintenance-tracker-api  
## [![Build Status](https://travis-ci.org/justinembawomye/tracker.svg?branch=master)](https://travis-ci.org/justinembawomye/tracker)   
This API  allows users to create, create accounts, login and make maintenance or repair requests to operations/repairs department and monitor the status of their respective requests

##  Required Features(Endpoints)
       
Endpoint | Functionality
-------- | -------------
POST/auth/register | Register a user
POST/auth/login | login a user
GET /api/v1/users/requests | Fetch all the requests of a logged in user
GET /api/v1/users/requests/`<requestId>` | Fetch a request that belongs to a logged in user
POST /api/v1/users/requests/ | Create a request
PUT /api/v1/users/requests/`<requestId>`/ | Modify a request.

##  Prerequisites
* Python/Flask framework


##  Technologies
* Python 3.6
* Flask Restful

##  Requirements
* Setup a virtual environment
* Install Python preferably version 3 and above
* pip install Flask
* pip install pytest

##  Run the app
Run python app.py on command prompt
* View the api on http://127.0.0.1:5000/auth/register
* Test it's usage with postman

## Import unittest library in the test file
* import Unittest
* write tests
* Run pytest on command prompt to see failing tests and after refactor to make the tests run

