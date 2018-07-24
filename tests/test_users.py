from tests import BaseTestCase
import json


class UserTestCase(BaseTestCase):
    
    def test_register_user(self):
        response = self.test_client.post('/auth/register', data=json.dumps(self.user_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("User Justine has been registered",str(response.data))



    def test_register_user_fail(self):
        """Ensures that a user with missing credentials is not registered"""
        response = self.test_client.post('/auth/register', content_type='application/json',
                            data=json.dumps({"email":"justine@gmail.com","username":"justine","password":"123456"}))
        self.assertEqual(response.status_code, 400)
    
    

    def test_user_login(self):
        response = self.test_client.post('/auth/login', data=json.dumps(self.user_login_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome Tinah. You are logged in",str(response.data))

    def test_login_without_password(self):
        response = self.test_client.post('/auth/login', data=json.dumps({"username":"Tinah", "password":" "}), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('password  is required',str(response.data))

    def test_login_without_username(self):
        response = self.test_client.post('/auth/login', data=json.dumps({"username":" ", "password":"123456"}), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('username is required',str(response.data))
        
    def test_register_user_with_invalid_email(self):
        response = self.test_client.post('/auth/register', data=json.dumps({"name":"Justine", "email":"justine.com", "username":"Tinah", "password":"123456"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Enter a valid email', str(response.data))    
    

        

     




