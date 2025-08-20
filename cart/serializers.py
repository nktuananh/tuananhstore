from rest_framework import serializers
# BẠN CẦN IMPORT CẢ PRODUCT VÀ CARTITEM
from .models import Product, CartItem


# Serializer MỚI cho Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image']


# Serializer CŨ cho CartItem (được sửa lại cho đúng)
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        # SỬA LẠI FIELDS CHO ĐÚNG VỚI MODEL MỚI
        # Nó không còn name, price, image nữa, thay vào đó là liên kết 'product'
        fields = ['id', 'product', 'size', 'quantity', 'added_at']