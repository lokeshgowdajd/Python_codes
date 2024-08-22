import unittest
import requests

class TestSmoke(unittest.TestCase):

    BASE_URL = "http://127.0.0.1:8080/"

    def test_home_page(self):
        response = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to the Home Page!", response.json()['message'])

    def test_login_page(self):
        response = requests.get(f"{self.BASE_URL}/login")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Login Page", response.json()['message'])

    def test_dashboard_page(self):
        response = requests.get(f"{self.BASE_URL}/dashboard")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Dashboard", response.json()['message'])

if __name__ == '__main__':
    unittest.main()
