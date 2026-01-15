from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product


class SearchViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Bracelets",
            slug="bracelets",
            description="Bracelet category",
        )

        self.product_match = Product.objects.create(
            name="Gold Bracelet",
            slug="gold-bracelet",
            description="Nice bracelet",
            category=self.category,
            price="29.00",
            stock=10,
            available=True,
        )
        self.product_no_match = Product.objects.create(
            name="Silver Ring",
            slug="silver-ring",
            description="Nice ring",
            category=self.category,
            price="19.00",
            stock=10,
            available=True,
        )

        self.product_unavailable = Product.objects.create(
            name="Gold Necklace",
            slug="gold-necklace",
            description="Nice necklace",
            category=self.category,
            price="49.00",
            stock=0,
            available=False,
        )
    def test_search_returns_products_that_match_query(self):
        """Search should return only available products that match query."""
        url = reverse("search")
        response = self.client.get(url, {"title": "Gold"})

        self.assertEqual(response.status_code, 200)

        # Should include matching available product
        self.assertContains(response, "Gold Bracelet")

        # Should NOT include non-matching product
        self.assertNotContains(response, "Silver Ring")

        # Should NOT include unavailable product even if it matches query
        self.assertNotContains(response, "Gold Necklace")

    def test_search_with_empty_query_returns_all_available_products(self):
        """Empty search should return all available products."""
        url = reverse("search")
        response = self.client.get(url, {"title": ""})

        self.assertEqual(response.status_code, 200)

        # All available products should show
        self.assertContains(response, "Gold Bracelet")
        self.assertContains(response, "Silver Ring")

        # Unavailable should not show
        self.assertNotContains(response, "Gold Necklace")
