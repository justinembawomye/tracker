from tests import BaseTestCase
import json
from api.models import User
class TestModels(BaseTestCase):

    def test_register_user(self):
        """ Endpoint to test register a user using the User class """
        user = User("Justine", "justine@gmail.com", "Tinah", "123456",1)
       