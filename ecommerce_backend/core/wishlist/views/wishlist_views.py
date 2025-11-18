from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.wishlist.models.wishlist import Wishlist
from core.wishlist.serializers.wishlist_serializer import WishlistSerializer

class WishlistViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request):
        wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
        return Response(WishlistSerializer(wishlist).data)

    def add(self, request):
        wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
        product_id = request.data.get("product_id")

        wishlist.products.add(product_id)
        return Response({"message": "Added to wishlist"})

    def remove(self, request):
        wishlist = request.user.wishlist
        product_id = request.data.get("product_id")

        wishlist.products.remove(product_id)
        return Response({"message": "Removed from wishlist"})

