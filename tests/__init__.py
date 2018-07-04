import unittest


from api.views import app

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client()
        self.user_data = {
            "id": 1,
            "name": "Justine",
            "email":"justine@gmail.com",
            "username":"Tinah",
            "password":"123456"
           
        }

    
    def tearDown(self):
        pass


    

if __name__ == "__main__":
    unittest.main()