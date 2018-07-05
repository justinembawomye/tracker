from tests import BaseTestCase
import json


class UserTestCase(BaseTestCase):
    
    def test_register_user(self):
        response = self.test_client.post('/auth/register', data=json.dumps(self.user_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("User Tinah has been registered",str(response.data))

    def test_user_login(self):
        response = self.test_client.post('/auth/login', data=json.dumps(self.user_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome Tinah. You are logged in",str(response.data))

        

     




