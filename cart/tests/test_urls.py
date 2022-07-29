from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.urls import *


class TestUrls(SimpleTestCase):

    def test_cart_detail_is_resolved(self):
        url = reverse('cart:cart_detail')
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, cart_detail)

    def test_cart_add_is_resolved(self):
        url = reverse('cart:cart_add', args=[1])
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, cart_add)

    def test_cart_remove_is_resolved(self):
        url = reverse('cart:cart_remove', args=[1])
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, cart_remove)
