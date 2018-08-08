from tests import BaseTestCase
import json


class UserTestCase(BaseTestCase):

    def test_register_user(self):
        response = self.test_client.post(
            '/auth/register', data=json.dumps(self.user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("User Justine has been registered", str(response.data))

    def test_register_with_no_data_provided(self):
        """Test user cannot register with no data provided"""
        response = self.test_client.post(
            '/auth/register', content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_empty_entry(self):
        """Test user cannot register with empty fields"""

        response = self.test_client.post(
            '/auth/register', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("All fields are required", str(response.data))

    def test_register_user_fail(self):
        """Ensures that a user with missing credentials is not registered"""

        response = self.test_client.post('/auth/register', content_type='application/json',
                                         data=json.dumps({"email": "justine@gmail.com", "username": "justine", "password": "123456"}))
        self.assertEqual(response.status_code, 400)

    def test_register_with_invalid_password(self):
        """Test user cannot register without a password"""

        response = self.test_client.post('/auth/register', data=json.dumps(
            {"name": "Justine", "email": "justine@gmail.com", "username": "Tinah", "password": "123"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('A stronger password  is required', str(response.data))

    def test_register_with_invalid_email(self):
        """Test user cannot register with an invalid email address"""
        response = self.test_client.post('/auth/register', data=json.dumps(
            {"name": "Justine", "email": "justine.com", "username": "Tinah", "password": "12356"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Enter a valid email', str(response.data))

    def test_register_user_with_invalid_username(self):
        """Test user cannot register with invalid username"""
        response = self.test_client.post('/auth/register', data=json.dumps(
            {"name": "Justine", "email": "justine@gmail.com", "username": "Tinah", "password": ""}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('A stronger password  is required', str(response.data))


        response = self.test_client.post('/auth/register', data=json.dumps(
            {"name": "Justine", "email": "justine@gmail.com", "username": " ", "password": "123456"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid username', str(response.data))

    def test_register_without_password(self):
        """Test user cannot register without providing a password"""

    def test_user_login(self):
        """Test user can login successfully"""

        response = self.test_client.post(
            '/auth/login', data=json.dumps(self.user_login_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome Tinah. You are logged in", str(response.data))

    def test_user_login_without_password(self):
        """Test user can't login without a password"""

        response = self.test_client.post('/auth/login', data=json.dumps(
            {"username": "Tinah", "password": " "}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('password  is required', str(response.data))

    def test_user_login_without_username(self):
        """Test user cannot login without a username"""

        response = self.test_client.post('/auth/login', data=json.dumps(
            {"username": " ", "password": "123456"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('username is required', str(response.data))
