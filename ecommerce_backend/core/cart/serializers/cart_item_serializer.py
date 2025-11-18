from rest_framework import serializers
from core.cart.models.cart_item import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'subtotal']

    def get_subtotal(self, obj):
        return obj.subtotal()

