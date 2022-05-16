from django.test import SimpleTestCase
from django.urls import reverse, resolve
from orders.urls import *


class TestUrls(SimpleTestCase):

    def test_create_order_is_resolved(self):
        url = reverse('orders:create_order')
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, create_order)
