
import unittest

from app import app


class BackendTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_returns_success(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_returns_expected_message(self):
        response = self.client.get("/")
        self.assertEqual(
            response.get_data(as_text=True),
            "Backend API is running!",
        )


if __name__ == "__main__":
    unittest.main()
