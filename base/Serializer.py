from rest_framework import serializers
from .models import Product, Category
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'