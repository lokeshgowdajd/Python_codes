# test_integration.py

import unittest
from auth import login
from user_data import get_user_data

class TestIntegration(unittest.TestCase):

    def test_login_and_get_user_data(self):
        # Test login
        token = login("admin", "admin")
        self.assertIsNotNone(token)

        # Test fetching user data with valid token
        user_data = get_user_data(token)
        self.assertIsNotNone(user_data)
        self.assertEqual(user_data['id'], 1)

        # Test fetching user data with invalid token
        user_data = get_user_data("invalid_token")
        self.assertIsNone(user_data)

if __name__ == '__main__':
    unittest.main()
