from django.shortcuts import render


from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response


from .authentication import TokenAuthentication
from .models import Token, Shop
from .serializers import ShopLoginSerializer, ShopSerializer

@api_view(['POST'])
def login(request):
    
    setializer = ShopLoginSerializer(data=request.POST)

    if setializer.is_valid():
        shop = Shop.objects.get(**setializer.data)
        token = Token.objects.create(shop=shop)
        
        return Response({'token': token.key, 'shop': ShopSerializer(shop).data}, status=200)
    else:
        return Response(setializer.errors, status=400)
    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def products(request):
    return Response(status=200)
    