from rest_framework import serializers
from core.wishlist.models.wishlist import Wishlist
from products.serializers.product_serializer import ProductSerializer

class WishlistSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'products']

