import datetime
from django.test import TestCase
from django.urls import reverse

class FooterYearTests(TestCase):
    def test_footer_displays_current_year(self):
        # Arrange
        current_year = datetime.date.today().year

        # Act
        response = self.client.get(reverse("home"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"© {current_year} Bella-Store")
