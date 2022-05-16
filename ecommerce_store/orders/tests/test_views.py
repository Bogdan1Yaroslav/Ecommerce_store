from django.test import TestCase, Client
from django.urls import reverse
from app_ecommerce_store.models import Profile, Category, Product, Promotion
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user_01',
                                             email='user_01@test.com',
                                             password='Somebody_password_01')

        self.logged_in = self.client.login(username='user_01', password='Somebody_password_01')

        self.profile = Profile.objects.create(user=self.user,
                                              date_of_birth="1990-10-10",
                                              city="Moscow",
                                              email="user@user.com",
                                              phone_number="+88805553535"
                                              )

    def test_create_order_GET(self):
        response = self.client.get(reverse("orders:create_order"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/create_order.html')


