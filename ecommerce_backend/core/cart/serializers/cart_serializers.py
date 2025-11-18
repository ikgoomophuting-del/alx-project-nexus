from rest_framework import serializers
from .cart_item_serializer import CartItemSerializer
from core.cart.models.cart import Cart

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total']

    def get_total(self, obj):
        return obj.total_price()

