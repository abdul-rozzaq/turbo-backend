

from django.forms import ValidationError
from rest_framework import serializers


from .models import Shop, Token


class ShopLoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    password = serializers.CharField(max_length=256)
    device = serializers.CharField(max_length=256, default='None')
    
    def validate(self, attrs):
        val = super().validate(attrs)
        
        name = attrs.get('name')
        password = attrs.get('password')
                        
        if not Shop.objects.filter(name=name, password=password).exists():
            raise ValidationError('Shop not found')
            
        return val
    
    
    def to_representation(self, instance):
        return super().to_representation(instance)
    
    


class ShopSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Shop
        exclude = ['password']


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
