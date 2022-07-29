from unittest import TestCase
from django.contrib.auth.models import User
from app_ecommerce_store.models import Profile, Category, Product, Promotion


class TestProfileModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Some_username_1',
                                        email='test@test.com')

        self.user.set_password('some_password123')
        self.user.save()

        self.test_profile = Profile.objects.create(user=self.user,
                                                   date_of_birth="1990-10-10",
                                                   city='New_york',
                                                   email='test@test.com',
                                                   phone_number="+00412214430000"
                                                   )

    def test(self):
        self.assertEqual(self.test_profile.user.username, self.user.username)
        self.user.delete()
        self.test_profile.delete()


class TestCategoryModel(TestCase):

    def setUp(self):
        self.category = Category.objects.create(category_name='Some_category_name',
                                                category_slug='some_category_name')

    def test(self):
        self.assertEqual(self.category.category_name, 'Some_category_name')
        self.assertEqual(self.category.category_slug, 'some_category_name')
        self.category.delete()


class TestProductModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Some_username_1',
                                        email='test@test.com')

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

    def test(self):
        self.assertEqual(self.product.product_name, 'Some product name')
        self.assertEqual(self.product.product_code, 'Some product code')
        self.assertEqual(self.product.product_slug, 'some-product-name')
        self.user.delete()
        self.category.delete()
        self.product.delete()


class TestPromotionModel(TestCase):

    def setUp(self):
        self.promotion = Promotion.objects.create(promotion_name='Some production name',
                                                  promotion_description='Some production description')

    def test(self):
        self.assertEqual(self.promotion.promotion_name, 'Some production name')
        self.assertEqual(self.promotion.promotion_description, 'Some production description')

        self.promotion.delete()
