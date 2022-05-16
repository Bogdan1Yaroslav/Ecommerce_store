from unittest import TestCase
from django.contrib.auth.models import User
from orders.models import Order, OrderItem
from app_ecommerce_store.models import Product, Profile, Category


class TestOrderModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Some_username_1',
                                        email='test@test.com')

        self.user.set_password('some_password123')
        self.user.save()

        self.test_profile = Profile.objects.create(user=self.user,
                                                   date_of_birth="1990-10-10",
                                                   city='New_york',
                                                   email='test@test.com',
                                                   phone_number="+00412232214430000"
                                                   )

        self.order = Order.objects.create(customer=self.test_profile)

    def test(self):
        self.assertEqual(self.order.customer, self.test_profile)

        self.user.delete()
        self.test_profile.delete()
        self.order.delete()


class TestOrderItemModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Some_username_1',
                                        email='test@test.com')

        self.user.set_password('some_password123')
        self.user.save()

        self.test_profile = Profile.objects.create(user=self.user,
                                                   date_of_birth="1990-10-10",
                                                   city='New_york',
                                                   email='test@test.com',
                                                   phone_number="+00412232214430000"
                                                   )

        self.order = Order.objects.create(customer=self.test_profile)

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

        self.order_item = OrderItem.objects.create(order=self.order,
                                                   product=self.product,
                                                   price=100,
                                                   quantity=1)

    def test(self):
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.price, 100)
        self.assertEqual(self.order_item.quantity, 1)

        self.user.delete()
        self.test_profile.delete()
        self.order.delete()
        self.category.delete()
        self.product.delete()
        self.order_item.delete()
