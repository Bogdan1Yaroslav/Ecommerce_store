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

        self.promotion = Promotion.objects.create(promotion_name='Some production name',
                                                  promotion_description='Some production description')

    def test_home_page(self):
        response = self.client.get(reverse("app_ecommerce_store:home"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce_store/home.html')

    def test_register_GET(self):
        response = self.client.get(reverse("app_ecommerce_store:register"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce_store/register.html')

    def test_register_POST(self):
        response = self.client.post(reverse("app_ecommerce_store:register"), {"username": "User_01",
                                                                              "first_name": "Jonh",
                                                                              "last_name": "James",
                                                                              "password1": "Somepassword_231",
                                                                              "password2": "Somepassword_231",
                                                                              "email": "jonh.james@gmail.com",
                                                                              "date_of_birth": "1990-10-10",
                                                                              "city": "Chicago",
                                                                              "phone_number": "+0000000000",
                                                                              })
        self.assertRedirects(response, reverse('app_ecommerce_store:home'))
        self.assertEquals(response.status_code, 302)

    def test_product_list(self):
        response = self.client.get(reverse("app_ecommerce_store:product_list"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce_store/product_list.html')

    def test_product_detail(self):
        response = self.client.get(reverse("app_ecommerce_store:product_detail", args=[self.product.id,
                                                                                       self.product.product_slug]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce_store/product_detail.html')

    def test_category_list(self):
        response = self.client.get(reverse("app_ecommerce_store:category_list"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce_store/category_list.html')

    def test_account(self):
        response = self.client.get(reverse("app_ecommerce_store:account"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce_store/account.html')

    def test_balance_refill_GET(self):
        response = self.client.get(reverse("app_ecommerce_store:balance_refill"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce_store/balance_refill.html')

    def test_balance_refill_POST(self):
        response = self.client.post(reverse("app_ecommerce_store:balance_refill"),
                                    {"deposit_money": 100})

        self.assertRedirects(response, reverse('app_ecommerce_store:account'))
        self.assertEquals(response.status_code, 302)

    def test_account_edit_GET(self):
        response = self.client.get(reverse("app_ecommerce_store:edit_account"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce_store/edit_account.html')

    def test_account_edit_POST(self):
        response = self.client.post(reverse("app_ecommerce_store:edit_account"),
                                    {"username": "user_02",
                                     "first_name": "Jonh",
                                     "last_name": "James",
                                     "date_of_birth": "1990-10-11",
                                     "city": "Chicago",
                                     "email": "user@1user.com",
                                     "phone_number": "+88805553535"
                                     })

        self.assertRedirects(response, reverse('app_ecommerce_store:account'))
        self.assertEquals(response.status_code, 302)
