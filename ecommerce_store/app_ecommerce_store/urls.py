from django.urls import path
from app_ecommerce_store.views import *

app_name = 'app_ecommerce_store'

urlpatterns = [

    # Login page
    path('login/', LogInView.as_view(), name="login"),

    # Logout page
    path('logout/', LogOutView.as_view(), name="logout"),

    # Register page
    path('register/', register_view, name="register"),

    # Home page
    path("", home, name="home"),

    # Product list
    path("product_list/", product_list, name="product_list"),

    # Product list by category
    path("product_list/<slug:category_slug>/", product_list, name="product_list_by_category"),

    # Product detail
    path("<int:id>/<slug:slug>/", product_detail, name="product_detail"),

    # Category list
    path("category_list/", category_list, name="category_list"),

    # Profile page
    path("account/", account, name="account"),

    # Account edit
    path('edit_account/', AccountEditFormView.as_view(), name="edit_account"),

    # Balance refill
    path("balance_refill/", balance_refill, name="balance_refill"),





]
