from unittest import TestCase
from cart.forms import CartAddProductForm


class TestCartAddProductForm(TestCase):
    def test_cart_add_product_form_is_valid(self):
        form = CartAddProductForm(data={"quantity": 1})

        self.assertTrue(form.is_valid())

    def test_cart_add_product_form_not_valid(self):
        form = CartAddProductForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
