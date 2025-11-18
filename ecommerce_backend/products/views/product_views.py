from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from users.permissions.roles_permissions import IsAdminOrReadOnly

from products.models import Product
from products.serializers.product_serializer import ProductSerializer
from products.filters.product_filters import ProductFilter
from products.pagination.product_pagination import ProductPagination


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    # Add filtering, sorting, search
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    # Filters
    filterset_class = ProductFilter

    # Sorting options
    ordering_fields = ["price", "name", "created_at"]
    ordering = ["-created_at"]  # default newest first

    # Search
    search_fields = ["name", "description"]


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    filterset_class = ProductFilter
    ordering_fields = ["price", "name", "created_at"]
    ordering = ["-created_at"]
    search_fields = ["name", "description"]

    # Only admins can POST new products
    permission_classes = [IsAdminOrReadOnly]


    class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Only Admins can update/delete
    permission_classes = [IsAdminOrReadOnly]


# Only admins can POST new products
    permission_classes = [IsAdminOrReadOnly]

