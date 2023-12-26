import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import random
from faker import Faker
from shop.models import MoneyHistory, Product, Shop

# ================================================================= #


fake = Faker()
shops = Shop.objects.all()


# for _ in range(10):
#     Shop.objects.create(
#         name=fake.word(),
#         password=fake.word()
#     )


for product in Product.objects.all():
    for _ in range(10):
        MoneyHistory.objects.create(
            product=product,
            count=random.randint(1, product.count)
        )

# def ajratish(data):
#     result = {}
#     for item in data:
#         item_type = item['type']
#         if item_type not in result:
#             result[item_type] = []
#         result[item_type].append(item)
#     return list(result.values())


# data = [
#     {'type': 'product'},
#     {'type': 'shop'},
#     {'type': 'product'},
#     {'type': 'shop'},
#     {'type': 'product'},
#     {'type': 'product'},
#     {'type': 'product'},
#     {'type': 'shop'},
#     {'type': 'product'},
#     {'type': 'product'},
# ]

# print(ajratish(data))
