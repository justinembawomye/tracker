# maintenance-tracker-api  
## [![Build Status](https://travis-ci.org/justinembawomye/tracker.svg?branch=challenge2)](https://travis-ci.org/justinembawomye/tracker) [![Coverage Status](https://coveralls.io/repos/github/justinembawomye/tracker/badge.svg?branch=challenge2)](https://coveralls.io/github/justinembawomye/tracker?branch=challenge2) [![Maintainability](https://api.codeclimate.com/v1/badges/94d5d010d5645258eb7c/maintainability)](https://codeclimate.com/github/justinembawomye/tracker/maintainability)

This API  allows users to create accounts, login and make maintenance or repair requests to operations/repairs department and monitor the status of their respective requests

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

##  Requirements
* Setup a virtual environment
* `pip install -r requirements.txt`

##  Run the app
Run python app.py on command prompt
* View the api on http://127.0.0.1:5000/auth/register
* Test it's usage with postman

## Import unittest library in the test file
* import Unittest
* write tests
* Run pytest on command prompt to see failing tests and after refactor to make the tests run

