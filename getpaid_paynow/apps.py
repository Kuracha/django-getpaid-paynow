from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GetpaidPaynowAppConfig(AppConfig):
    name = "getpaid_paynow"
    verbose_name = _("mBank Paynow")

    def ready(self):
        from getpaid.registry import registry

        registry.register(self.module)
