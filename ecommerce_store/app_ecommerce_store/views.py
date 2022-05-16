from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from app_ecommerce_store.forms import RegisterForm, BalanceRefillForm, UserForm, ProfileForm
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from app_ecommerce_store.models import Profile, Category, Product, Promotion
from orders.models import Order
from django.views.generic import DetailView
from django.db.models import Q
from django.urls import reverse
from cart.forms import CartAddProductForm

from django.core.cache import cache


# ----------------------------------------------------------------------------------------
# Home page
def home(request):
    products = Product.objects.all()[:6]

    return render(request, "ecommerce_store/home.html", {"products": products})


# ----------------------------------------------------------------------------------------------------------------------
# Login
class LogInView(LoginView):
    template_name = "ecommerce_store/login.html"


# Logout
class LogOutView(LogoutView):
    next_page = "/"


# ----------------------------------------------------------------------------------------------------------------------
#  User registration
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get("date_of_birth")
            city = form.cleaned_data.get("city")
            email = form.cleaned_data.get("email")
            phone_number = form.cleaned_data.get("phone_number")

            Profile.objects.create(user=user,
                                   date_of_birth=date_of_birth,
                                   city=city,
                                   email=email,
                                   phone_number=phone_number
                                   )

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "ecommerce_store/register.html", {"form": form})


# ----------------------------------------------------------------------------------------------------------------------
# Products list
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(product_available=True)
    if category_slug:
        category = get_object_or_404(Category, category_slug=category_slug)
        products = Product.objects.filter(product_category=category)
    return render(request, "ecommerce_store/product_list.html",
                  {'category': category,
                   'categories': categories,
                   'products': products})


# ----------------------------------------------------------------------------------------------------------------------
# Product detail
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, product_slug=slug, product_available=True)
    cart_product_form = CartAddProductForm()

    context = {'product': product, 'cart_product_form': cart_product_form}

    return render(request, "ecommerce_store/product_detail.html", context)


# ----------------------------------------------------------------------------------------------------------------------
# Categories list
def category_list(request):
    categories = Category.objects.all()

    return render(request, "ecommerce_store/category_list.html", {'categories': categories})


# ----------------------------------------------------------------------------------------------------------------------
# User profile
def account(request):
    profile = Profile.objects.get(user=request.user.id)
    profile_deposit = profile.deposit

    customer_orders = Order.objects.filter(customer=profile)

    special_offers_cache_key = 'special_offers:{}'.format(profile)
    promotions_cache_key = 'promotions:{}'.format(profile)

    special_offers = Product.objects.filter(product_price__lte=profile_deposit)[:5]

    promotions = Promotion.objects.all()

    user_account_cache_data = {
        special_offers_cache_key: special_offers,
        promotions_cache_key: promotions

    }

    cache.set_many(user_account_cache_data)

    context = {'customer_orders': customer_orders, 'promotions': promotions, 'special_offers': special_offers}

    return render(request, "ecommerce_store/account.html", context)


# ----------------------------------------------------------------------------------------------------------------------
# Refill balance
def balance_refill(request):
    profile_id = request.user.id

    profile = Profile.objects.get(user=profile_id)
    balance_refill_form = BalanceRefillForm()

    if request.method == 'POST':
        balance_refill_form = BalanceRefillForm(request.POST)
        if balance_refill_form.is_valid():
            money_to_deposit = balance_refill_form.cleaned_data["deposit_money"]

            profile.deposit += money_to_deposit
            profile.save()

            return HttpResponseRedirect(reverse('app_ecommerce_store:account'))

    context = {'balance_refill_form': balance_refill_form}

    return render(request, "ecommerce_store/balance_refill.html", context)


# ----------------------------------------------------------------------------------------------------------------------
# Account edit
class AccountEditFormView(View):

    def get(self, request):
        # if not request.user.has_perm("app_news.change_news"):  # ОТРЕДАКТИРОВАТЬ!!!!
        #     raise PermissionDenied()
        profile = Profile.objects.get(user=request.user.id)

        user_form = UserForm(instance=request.user)

        profile_form = ProfileForm(instance=profile)

        context = {"profile_form": profile_form, "user_form": user_form}

        return render(request, "ecommerce_store/edit_account.html", context)

    def post(self, request):
        profile = Profile.objects.get(user=request.user.id)

        user_form = UserForm(request.POST, instance=request.user)

        profile_form = ProfileForm(request.POST, instance=profile)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile.save()
            return HttpResponseRedirect(reverse('app_ecommerce_store:account'))

        context = {"profile_form": profile_form, "user_form": user_form}

        return render(request, "ecommerce_store/edit_account.html", context)

# ----------------------------------------------------------------------------------------------------------------------
