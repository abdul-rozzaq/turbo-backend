from django.contrib import admin

from .models import Shop, Token



class TokenAdmin(admin.ModelAdmin):
    list_display = ['key', 'device', 'shop']
    list_filter = ['shop']
    

admin.site.register(Shop)
admin.site.register(Token, TokenAdmin)
