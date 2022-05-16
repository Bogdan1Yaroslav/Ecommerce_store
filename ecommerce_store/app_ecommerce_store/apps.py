from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppEcommerceStoreConfig(AppConfig):
    name = 'app_ecommerce_store'
    verbose_name = _('ecommerce_store')
