from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]

class ProductSerializer(serializers.ModelSerializer):
    tags =  TagSerializer(many=True)
    class Meta:
        model = Product
        fields = ['name','id', 'tags']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'id', 'email', 'phone']


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = ['status', 'customer', 'product']

