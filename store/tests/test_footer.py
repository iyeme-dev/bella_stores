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

class FooterLinksTests(TestCase):
    def test_footer_about_link_points_to_about_page(self):
        # Act
        resp = self.client.get(reverse("home"))
        about_url = reverse("about")

        # Assert
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, f'href="{about_url}"')