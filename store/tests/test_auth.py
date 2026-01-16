from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class SignInFeedbackTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="correct-password",
            email="test@example.com"
        )

    def test_wrong_login_shows_helpful_error_message(self):
        """
        Wrong credentials should show a visible error message to the user.
        """
        url = reverse("signin")
        response = self.client.post(url, {
            "username": "testuser",
            "password": "wrong-password",
        })

        # Page should re-render (not redirect)
        self.assertEqual(response.status_code, 200)

        # This should be visible somewhere in the HTML
        self.assertContains(response, "Please enter a correct username and password", html=False)
