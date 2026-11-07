import unittest

# Import the app object and the shared items list from app.py
from app import app, items


class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        # Setup a test client to mock HTTP requests
        self.client = app.test_client()

        # Reset the global in-memory database to a clean state before every test
        items.clear()
        items.append({"id": 1, "name": "Laptop", "price": 999.99})

    def test_get_items(self):
        response = self.client.get("/api/items")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_create_item(self):
        payload = {"name": "Smartphone", "price": 499.99}
        response = self.client.post("/api/items", json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["name"], "Smartphone")


if __name__ == "__main__":
    unittest.main()
