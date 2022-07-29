from unittest import TestCase
from app_ecommerce_store.forms import AuthForm, RegisterForm, UserForm, ProfileForm, BalanceRefillForm


class TestAuthForm(TestCase):
    def test_auth_form_is_valid(self):
        form = AuthForm(data={
            "username": "User_01",
            "password": "Some_password_231"
        })

        self.assertTrue(form.is_valid())

    def test_auth_form_not_valid(self):
        form = AuthForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


class TestRegisterForm(TestCase):

    def test_register_form_is_valid(self):
        form = RegisterForm(data={"username": "User_01",
                                  "first_name": "Jonh",
                                  "last_name": "James",
                                  "password1": "Some_password_231",
                                  "password2": "Some_password_231",
                                  "email": "jonh.james@gmail.com",
                                  "date_of_birth": "10/10/1990",
                                  "city": "Chicago",
                                  "phone_number": "+0000000000",
                                  })

        self.assertTrue(form.is_valid())

    def test_register_form_not_valid(self):
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 9)


class TestUserForm(TestCase):

    def test_user_form_is_valid(self):
        form = UserForm(data={"username": "User_name_01",
                              "first_name": "Jonh",
                              "last_name": "James"})

        self.assertTrue(form.is_valid())

    def test_user_form_not_valid(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)


class TestProfileForm(TestCase):

    def test_profile_form_is_valid(self):
        form = ProfileForm(data={"date_of_birth": "1990-10-10",
                                 "city": "Moscow",
                                 "email": "test@test.com",
                                 "phone_number": "+88888888"})

        self.assertTrue(form.is_valid())

    def test_profile_form_not_valid(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)


class TestBalanceRefillForm(TestCase):

    def test_profile_form_is_valid(self):
        form = BalanceRefillForm(data={"deposit_money": 100})

        self.assertTrue(form.is_valid())

    #
    def test_profile_form_not_valid(self):
        form = BalanceRefillForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
