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
