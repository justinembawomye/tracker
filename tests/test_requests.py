from tests import BaseTestCase
import json


class RequestTestCase(BaseTestCase):
    
    def test_create_request(self):
        """ Tests whether a user can create a request successfully """

        response = self.test_client.post('/api/v1/users/requests', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Hey kiz! You have successfully created a request",str(response.data))

    def test_get_all_requests(self):
        """ Tests whether a user can fetch all his/her requests successfully """

        response = self.test_client.post('/api/v1/users/requests', data=json.dumps(self.request_data), content_type = 'application/json')
        response = self.test_client.get('/api/v1/users/requests', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 302)
          
    def test_get_single_request(self):
        """ Tests  whether a single request can be returned by id successfully """
        response = self.test_client.get('/api/v1/users/requests/1', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        
                



    

