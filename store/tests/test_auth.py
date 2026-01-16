from django.test import TestCase
from django.urls import reverse

class AuthTests(TestCase):
    def test_invalid_login_shows_custom_error_message(self):
        url = reverse("signin")

        response = self.client.post(url, {
            "username": "wronguser",
            "password": "wrongpass",
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Invalid username or password. Please try again.",
            html=False
        )