from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order num: {order_id}'
    message = f'Dear {order.first_name}\n\n' \
              f'Your order id is {order_id}.'

    mail_send = send_mail(subject, message, 'admin@ecommerce_store.com', [order.mail])
    return mail_send


@shared_task
def multiply():
    print(7 * 7)