from django.contrib import admin
from .models import MoneyHistory, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count', 'type']
    list_filter = ['shop']

class MoneyHistoryAdmin(admin.ModelAdmin):
    list_display = [] + [x.name for x in MoneyHistory._meta.fields if x.name not in ['id', 'pk']]
    list_filter = ['product']
    
admin.site.register(Product, ProductAdmin)
admin.site.register(MoneyHistory, MoneyHistoryAdmin)
