from tests import BaseTestCase
import json
from api.models import User
class TestModels(BaseTestCase):

    def test_register_user(self):
        """ Endpoint to test register a user using the User class """
        new_user = User("Justine", "justine@gmail.com", "Tinah", "123456", 1)
        self.assertEqual(new_user.name, "Justine")
        self.assertEqual(new_user.email, "justine@gmail.com")
        self.assertEqual(new_user.username, "Tinah")
        self.assertEqual(new_user.password, "123456")
        self.assertEqual(new_user.user_id, 1)