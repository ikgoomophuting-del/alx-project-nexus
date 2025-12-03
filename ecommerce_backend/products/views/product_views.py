# products/views/product_views.py

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from users.permissions.roles_permissions import IsAdminOrReadOnly
from products.models.product import Product
from products.serializers.product_serializers import ProductSerializer
from products.filters.product_filters import ProductFilter
from products.pagination.product_pagination import ProductPagination


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related("category", "owner").all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    filterset_class = ProductFilter
    ordering_fields = ["price", "name", "created_at"]
    ordering = ["-created_at"]
    search_fields = ["name", "description"]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related("category", "owner").all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
