from django.db import models
from app_ecommerce_store.models import Product, Profile
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Customer'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return round(sum(float(item.get_cost()) for item in self.items.all()), 2)


# ----------------------------------------------------------------------------------------------------------------------

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return str(self.price * self.quantity)
