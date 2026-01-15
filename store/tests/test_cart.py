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

    def test_add_cart_creates_cart_item_and_redirects(self):
        """Adding a product should create a Cart + CartItem and redirect to cart page."""
        add_url = reverse("add_cart", args=[self.product.id])

        response = self.client.get(add_url)

        # 1) it should redirect to cart_detail
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("cart_detail"))

        # 2) item exists
        cart_item = CartItem.objects.get(product=self.product)
        self.assertEqual(cart_item.quantity, 1)
