from django.urls import path

from .views import *


urlpatterns = [
    path('login/', login),
    path('products/', products),
    path('tokens/<int:shop_id>/', get_tokens),
    path('delete-token/<str:token_id>/', delete_token),
    path('money-histories/<int:pk>/', money_histories),
]
