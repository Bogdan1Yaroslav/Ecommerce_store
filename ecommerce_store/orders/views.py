from django.shortcuts import render, redirect
from django.urls import reverse
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created, multiply


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user.profile
            order.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            # order_created.delay(order.id)
            # multiply()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
            # return render(request, 'orders/created.html', {'order': order})

    else:
        form = OrderCreateForm()

    return render(request, 'orders/create_order.html', {'cart': cart, 'form': form})
