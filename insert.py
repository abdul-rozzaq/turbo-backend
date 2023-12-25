import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# ================================================================= #
from shop.models import Product, Shop
from faker import Faker

import random

fake = Faker()
shops = Shop.objects.all()


for _ in range(10):
    Shop.objects.create(
        name=fake.word(),
        password=fake.word()
    )


for shop in Shop.objects.all():
    for _ in range(10):
        Product.objects.create(
            shop=shop,
            name=fake.word(),
            price=random.randint(15, 150),
            count=random.randint(20, 100) * 1000,
            type=fake.random_element(elements=('1', '4', '2', '3'))
        )

