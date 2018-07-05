from tests import BaseTestCase
import json


class RequestTestCase(BaseTestCase):
    
    def test_create_request(self):
        """ Tests whether a user can create a request successfully """

        response = self.test_client.post('/api/v1/users/requests', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Hey kiz! You have successfully created a request",str(response.data))

    

