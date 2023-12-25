from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count', 'type']
    list_filter = ['shop']



admin.site.register(Product, ProductAdmin)
