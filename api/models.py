from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.models import Shop

import binascii, os

class Token(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True, editable=False)
    shop = models.ForeignKey(Shop, related_name='auth_tokens', on_delete=models.CASCADE, verbose_name=_("User"))

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        self.key = self.generate_key()

        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
