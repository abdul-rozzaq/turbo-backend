from collections.abc import Iterable
from django.db import models
import datetime


class Shop(models.Model):
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    name = models.CharField(max_length=256)
    price = models.FloatField()
    count = models.IntegerField()
    type = models.CharField(choices={
        '1': 'dona',
        '4': 'kg',
        '2': 'm2',
        '3': 'm3',
    }, max_length=256)

    def __str__(self) -> str:
        return self.name


class MoneyHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=256)
    product_price = models.IntegerField()
    count = models.FloatField()
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = 'Money History'
        verbose_name_plural = 'Money Histories'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.product_name = self.product.name
            self.product_price = self.product.price
            self.created_at = datetime.datetime.now()

        return super().save(*args, **kwargs)

    @property
    def total_price(self):
        return self.product_price * self.count

    def __str__(self) -> str:
        return self.product_name
