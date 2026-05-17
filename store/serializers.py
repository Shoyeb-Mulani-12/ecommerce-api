from rest_framework import serializers
from .models import (
    Product,
    Category,
    Cart,
    CartItem,
    Order,
    OrderItem
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(
        source='cartitem_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items']


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(
        source='orderitem_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'is_paid', 'items']