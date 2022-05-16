from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# ----------------------------------------------------------------------------------------------------------------------
# Prodile model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("user"))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_("birth date"))
    city = models.CharField(max_length=36, blank=True, verbose_name=_("city"))
    email = models.EmailField(max_length=30, blank=True, verbose_name=_("email"))
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, blank=True,
                                    verbose_name=_("telephone"))

    deposit = models.PositiveIntegerField(default=0, verbose_name=_("Deposit"))

    class Meta:
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')

    def __str__(self):
        return str(self.user.username)


# ----------------------------------------------------------------------------------------------------------------------
# Category model

class Category(models.Model):
    category_name = models.CharField(max_length=200, db_index=True, verbose_name=_("Category name"))
    category_slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug")

    class Meta:
        ordering = ('category_name',)
        verbose_name_plural = _('categories')
        verbose_name = _('category')

    def __str__(self):
        return str(self.category_name)

    def get_absolute_url(self):
        return reverse('app_ecommerce_store:product_list_by_category', args=[self.category_slug])


# ----------------------------------------------------------------------------------------------------------------------
# Product model

class Product(models.Model):
    product_name = models.CharField(max_length=2000, db_index=True, verbose_name=_("Product name"))
    product_code = models.CharField(max_length=10, verbose_name=_("Product code"))
    product_slug = models.SlugField(max_length=200, db_index=True, verbose_name=_("Slug"))
    product_seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                       verbose_name=_('Product seller'))
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Product price in $"))
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True,
                                         verbose_name=_("Category name"))
    product_description = models.TextField(blank=True, verbose_name=_("Product description"))

    product_available = models.BooleanField(default=True)

    product_creation_date = models.DateField(auto_now_add=True, verbose_name=_("Product creation date"))
    updated = models.DateField(auto_now=True, verbose_name=_("Updated"))
    product_images = models.ImageField(upload_to="files/products/%Y/%m/%d", blank=True)

    class Meta:
        ordering = ('product_name',)
        index_together = (('id', 'product_slug'),)

        verbose_name_plural = _('products')
        verbose_name = _('product')

    def __str__(self):
        return str(self.product_name)

    def get_absolute_url(self):
        return reverse('app_ecommerce_store:product_detail', args=[self.id, self.product_slug])


# ----------------------------------------------------------------------------------------------------------------------
# Promotion model

class Promotion(models.Model):
    promotion_name = models.CharField(max_length=200, verbose_name=_("Promotion name"))
    promotion_description = models.CharField(max_length=2000, verbose_name=_("Promotion description"))
    promotion_creation_date = models.DateField(auto_now_add=True, verbose_name=_("Promotion creation date"))

    def __str__(self):
        return self.promotion_name

    class Meta:
        verbose_name_plural = _('promotions')
        verbose_name = _('promotion')
