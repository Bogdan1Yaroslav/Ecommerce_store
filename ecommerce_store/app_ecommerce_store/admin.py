from django.contrib import admin
from app_ecommerce_store.models import Category, Product, Profile, Promotion
from django.utils.translation import gettext_lazy as _


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "date_of_birth",
        "city",
        "deposit"
    ]

    list_filter = [
        "date_of_birth",
        "city"
    ]

    # search_fields = ["city"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['category_name', 'category_slug']

    prepopulated_fields = {'category_slug': ('category_name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = [
        'product_name',
        'product_code',
        'product_slug',
        'product_price',
        'product_category',
        'product_description',
        'product_available',
        'product_creation_date',
        'updated'
    ]

    list_filter = [
        'product_category',
        'product_available',
        'product_creation_date',
        'updated'
    ]

    list_editable = [
        'product_price',
        'product_available'
    ]

    prepopulated_fields = {'product_slug': ('product_name',)}


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):

    list_display = [
        'promotion_name',
        'promotion_description',
        'promotion_creation_date',
    ]

    list_filter = [
        'promotion_creation_date'
    ]
