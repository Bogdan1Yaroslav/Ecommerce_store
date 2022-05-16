from unittest import TestCase
from orders.forms import OrderCreateForm
from django.contrib.auth.models import User
from app_ecommerce_store.models import Profile


class TestOrderCreateForm(TestCase):
    def test_auth_form_is_valid(self):
        self.user = User.objects.create(username='Some_username_132',
                                        email='test@test.com')

        self.user.set_password('some_password123')
        self.user.save()

        self.test_profile = Profile.objects.create(user=self.user,
                                                   date_of_birth="1990-10-10",
                                                   city='New_york',
                                                   email='test@test.com',
                                                   phone_number="+00412232214430000"
                                                   )

        form = OrderCreateForm(data={})

        self.assertTrue(form.is_valid())

        self.user.delete()
        self.test_profile.delete()


