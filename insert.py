import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# ================================================================= #
from shop.models import Product, Shop
from faker import Faker


fake = Faker()
shops = Shop.objects.all()


# for _ in range(5):
#     Shop.objects.create(
#         name=fake.word(),
#         password=fake.word()
#     )


# for shop in Shop.objects.all():
#     for _ in range(10):
#         Product.objects.create(
#             shop=shop,
#             name=fake.word(),
#             price=fake.random_number(),
#             count=fake.random_number(),
#             type=fake.random_element(elements=('1', '4', '2', '3'))
#         )

import random

for pr in Product.objects.all():
    
    pr.count = random.randint(15, 150)
    pr.price = random.randint(20, 100) * 1000
    
    
    
    pr.save()