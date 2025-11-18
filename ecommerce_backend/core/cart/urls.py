from django.urls import path
from core.cart.views.cart_views import CartViewSet

cart = CartViewSet.as_view({
    'get': 'retrieve'
})

add_item = CartViewSet.as_view({
    'post': 'add_item'
})

remove_item = CartViewSet.as_view({
    'post': 'remove_item'
})

urlpatterns = [
    path('', cart, name='cart'),
    path('add/', add_item, name='add-item'),
    path('remove/', remove_item, name='remove-item'),
]

