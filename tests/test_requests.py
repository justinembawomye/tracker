from tests import BaseTestCase
import json


class RequestTestCase(BaseTestCase):

    def test_create_request(self):
        """ Tests whether a user can create a request successfully """

        response = self.test_client.post(
            '/api/v1/users/requests', data=json.dumps(self.request_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(
            "Hey kiz! You have successfully created a request", str(response.data))

    def test_create_request_with_empty_fields(self):
        """Tests user can\'t send request with empty fields"""
        response = self.test_client.post(
            '/api/v1/users/requests', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("All fields are required", str(response.data))

    def test_create_request_without_client_name(self):
        """ Test for create request without client name """
        with self.test_client:
            response = self.test_client.post('/api/v1/users/requests', content_type='application/json',
                                             data=json.dumps({"client_name": "", "email": "deekiz@gmail.com", "category": "repair", "request_title": "please repair my pc",
                                                              "description": "Hey! could you please repair my pc by noon", "department": "management"}))
            reply = json.loads(response.data)
            self.assertEqual(reply["message"], "client name is required")
            self.assertEqual(response.status_code, 400)

    def test_create_request_without_request_title(self):
        """ Test for create request with empty request title"""
        with self.test_client:
            response = self.test_client.post('/api/v1/users/requests', content_type='application/json',
                                             data=json.dumps({"client_name": "kiz", "email": "deekiz@gmail.com", "category": "repair", "request_title": "",
                                                              "description": "Hey! could you please repair my pc by noon", "department": "management"}))
            self.assertEqual(response.status_code, 400)
            self.assertIn('request title field is missing', str(response.data))

    def test_create_request_without_description(self):
        """ Test for create request with missing description """
        with self.test_client:
            response = self.test_client.post('/api/v1/users/requests', content_type='application/json',
                                             data=json.dumps({"client_name": "kiz", "email": "deekiz@gmail.com", "category": "repair", "request_title": "Repair my pc",
                                                              "description": "", "department": "management"}))
            self.assertEqual(response.status_code, 400)
            self.assertIn('Description is missing', str(response.data))

    def test_create_request_without_department(self):
        """ Test for create request with missing department field """
        with self.test_client:
            response = self.test_client.post('/api/v1/users/requests', content_type='application/json',
                                             data=json.dumps({"client_name": "kiz", "email": "deekiz@gmail.com", "category": "repair", "request_title": "Repair my pc",
                                                              "description": "Hey! could you please repair my pc by noon", "department": ""}))
            self.assertEqual(response.status_code, 400)
            self.assertIn('department field  is missing', str(response.data))

    def test_get_all_requests(self):
        """ Tests whether a user can fetch all his/her requests successfully """
        response = self.test_client.post(
            '/api/v1/users/requests', data=json.dumps(self.request_data), content_type='application/json')
        response = self.test_client.get(
            '/api/v1/users/requests', data=json.dumps(self.request_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_request(self):
        """ Tests  whether a request can be returned by id successfully """

        response = self.test_client.get('/api/v1/users/requests/1', data=json.dumps(self.request_data),
                                        content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_request_with_invalid_id(self):
        """Tests a user can\'t get a request with invalid id"""
        response = self.test_client.post('/api/v1/users/requests')
        response = self.test_client.get('/api/v1/users/requests/5', data=json.dumps(self.request_data),
                                        content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Request Not Found", str(response.data))

    def test_get_single_request_unavailable(self):
        """ Tests  whether a user can retrieve a request with an id that doesn't exist """
        self.test_client.post(
            '/api/v1/users/requests', data=json.dumps(self.request_data),
            content_type='application/json')
        self.test_client.get(
            '/api/v1/users/requests', data=json.dumps(self.request_data), content_type='application/json')
        response = self.test_client.get(
            '/api/v1/users/requests/6', content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Request Not Found', str(response.data))

    def test_request_with_missing_credentials(self):
        """Tests user can\'t send request with missing details"""
        response = self.test_client.post('/api/v1/users/requests',
                                         data=json.dumps({"client_name": "kiz", "email": "deekiz@gmail.com",
                                                          "category": "repair", "request_title": "please repair my pc",
                                                          "description": "Hey! could you please repair my pc by noon", "department": ""}),
                                         content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_create_request_with_invalid_email(self):
        response = self.test_client.post('/api/v1/users/requests',
                                         data=json.dumps({"client_name": "kiz", "email": "deekiz.com", "category": "repair",
                                                          "request_title": "please repair my pc", "description": "Hey! could you please repair my pc by noon",
                                                          "department": "control"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Enter a valid email', str(response.data))
