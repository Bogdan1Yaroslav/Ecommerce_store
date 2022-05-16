from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_ecommerce_store.urls import *


class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('app_ecommerce_store:login')
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func.view_class, LogInView)

    def test_logout_url_is_resolved(self):
        url = reverse('app_ecommerce_store:logout')
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func.view_class, LogOutView)

    def test_register_url_is_resolved(self):
        url = reverse('app_ecommerce_store:register')
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, register_view)

    def test_home_url_is_resolved(self):
        url = reverse('app_ecommerce_store:home')
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, home)

    def test_product_list_url_is_resolved(self):
        url = reverse('app_ecommerce_store:product_list')
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, product_list)

    def test_product_list_by_category_url_is_resolved(self):
        url = reverse('app_ecommerce_store:product_list_by_category', args=['some_category_slug'])
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, product_list)

    def test_product_detail_url_is_resolved(self):
        url = reverse('app_ecommerce_store:product_detail', args=[3, 'some_product_slug'])
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, product_detail)

    def test_category_list_url_is_resolved(self):
        url = reverse('app_ecommerce_store:category_list')
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, category_list)

    def test_account_url_is_resolved(self):
        url = reverse('app_ecommerce_store:account')
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, account)

    def test_balance_refill_url_is_resolved(self):
        url = reverse('app_ecommerce_store:balance_refill')
        # print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, balance_refill)
