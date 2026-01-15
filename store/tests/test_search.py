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
