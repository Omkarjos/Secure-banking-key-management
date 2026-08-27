import unittest
from app import app

class ApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)

    def test_incidents(self):
        response = self.client.get("/api/incidents")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
