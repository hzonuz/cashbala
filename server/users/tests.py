from django.test import TestCase


# Create your tests here.
class TestSignUp(TestCase):
    def test_signup(self):
        response = self.client.post(
            "/users/signup/v0/",
            {
                "username": "testuser",
                "password": "Test1234!",
                "email": "test@gmail.com",
                "first_name": "Test",
                "last_name": "User"
            },
            content_type="application/json",
        )
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["username"], "testuser")
        self.assertEqual(response.data["email"], "test@gmail.com")
        self.assertEqual(response.data["first_name"], "Test")
        self.assertEqual(response.data["last_name"], "User")
