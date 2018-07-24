from tests import BaseTestCase
import json
from api.models import User, Request
class TestModels(BaseTestCase):

    def test_register_user(self):
        """ Endpoint to test register a user using the User class """
        user = User("Justine", "justine@gmail.com", "Tinah", "123456",1)
    def test_create_request(self):
        """ Endpoint to test create request with the Request class """
        request = Request("Dee", "deekiz@gmail.com", "repair", "please repair my pc",
         "Hey! could you please repair my pc by noon", "control", 1)
