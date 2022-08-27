from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_ecommerce_store.models import Profile
from django.utils.translation import gettext_lazy as _


# ----------------------------------------------------------------------------------------------------------------------
# Authentication form

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# ----------------------------------------------------------------------------------------------------------------------
# Registration form

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=30, required=True)
    date_of_birth = forms.DateField(required=True, help_text=_("example: 1990-10-10"))
    city = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(required=True, help_text=_("example: +0000000000"))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")


# ----------------------------------------------------------------------------------------------------------------------
# User form

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")


# ----------------------------------------------------------------------------------------------------------------------
# Profile form

class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=False, input_formats=['%Y-%m-%d'])

    class Meta:
        model = Profile
        fields = ("date_of_birth", "city", "email", "phone_number")


# ----------------------------------------------------------------------------------------------------------------------
# Balance refill form

class BalanceRefillForm(forms.Form):
    deposit_money = forms.IntegerField(help_text=_("Please enter positive value"))
