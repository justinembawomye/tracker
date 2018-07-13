from api.views import app
import unittest

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client()
        self.user_data = {
            "user_id": 1,
            "name": "Justine",
            "email":"justine@gmail.com",
            "username":"Tinah",
            "password":"123456"
           
        }
        self.user_login_data={
            "username":"Tinah",
            "password":"123456"
        }
        self.request_data = {
            "request_id":1,
            "client_name":"kiz",
            "email":"deekiz@gmail.com",
            "category":"repair",
            "request_title":"please repair my pc",
            "description":"Hey! could you please repair my pc by noon",
            "department":"control"
        }

    
    def tearDown(self):
        pass


    

if __name__ == "__main__":
    unittest.main()