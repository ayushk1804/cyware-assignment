from app import app
import unittest

class Test_Flask_App(unittest.TestCase):
    def test_health_endpoint(self):
        """
        Check Whether Response is 200
        """
        tester = app.test_client(self)
        response = tester.get("/health_check")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_base_response(self):
        """
        Check Whether Response of / is Hi Team
        """
        tester = app.test_client(self)
        response = tester.get("/")
        message = response.data.decode()
        self.assertEqual(message, "Hi Team")