import unittest
from app import create_app

class APITest(unittest.TestCase):

    def setUp(self):

        self.app=create_app().test_client()

    def test_login(self):

        response=self.app.post("/api/login",
        json={
        "username":"yuvaraj",
        "password":"12345"
        })

        self.assertEqual(response.status_code,200)


if __name__=="__main__":
    unittest.main()