from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.cart.models.cart import Cart
from core.cart.models.cart_item import CartItem
from core.cart.serializers.cart_serializer import CartSerializer

class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def add_item(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get("product_id")
        qty = int(request.data.get("quantity", 1))

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product_id=product_id
        )
        item.quantity += qty
        item.save()

        return Response({"message": "Item added to cart"})

    def remove_item(self, request):
        cart = request.user.cart
        item_id = request.data.get("item_id")
        CartItem.objects.filter(id=item_id, cart=cart).delete()

        return Response({"message": "Item removed from cart"})

