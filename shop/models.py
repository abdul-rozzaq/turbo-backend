from django.db import models


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
