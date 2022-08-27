from django.test import TestCase, Client
from django.urls import reverse
from app_ecommerce_store.models import Profile, Category, Product
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

        self.category = Category.objects.create(category_name='Some_category_name',
                                                category_slug='some_category_name')

        self.product = Product.objects.create(product_name='Some product name',
                                              product_code='Some product code',
                                              product_slug='some-product-name',
                                              product_seller=self.user,
                                              product_price=100,
                                              product_category=self.category,
                                              product_description='Some description',

                                              product_images="media/files/products/2022/05/09/basket.png")

    def test_cart_add_POST(self):
        response = self.client.post(reverse("cart:cart_add", args=[self.product.id]), {"quantity": 1})

        self.assertRedirects(response, reverse('cart:cart_detail'))
        self.assertEquals(response.status_code, 302)

    def test_cart_remove(self):
        response = self.client.post(reverse("cart:cart_add", args=[self.product.id]))

        self.assertRedirects(response, reverse('cart:cart_detail'))
        self.assertEquals(response.status_code, 302)

    def test_cart_detail(self):
        response = self.client.post(reverse("cart:cart_detail"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_detail.html')
