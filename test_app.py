import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get('/')
        self.assertEqual(response.data, b"Hello, World!")

    def test_add(self):
        response = self.client.get('/add/2/3')
        self.assertEqual(response.data, b'5')

if __name__ == '__main__':
    unittest.main()

