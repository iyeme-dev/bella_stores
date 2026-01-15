from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product, Cart, CartItem


class CartTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Bracelet",
            slug="bracelet"
        )
        self.product = Product.objects.create(
            name="Gold Bracelet",
            slug="gold-bracelet",
            description="Test product",
            category=self.category,
            price=29.00,
            stock=10,
            available=True,
        )