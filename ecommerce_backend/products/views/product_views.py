from rest_framework import viewsets, filters
from products.models.product import Product
from products.serializers.product_serializer import ProductSerializer
from products.pagination.product_pagination import ProductPagination
from products.filters.product_filters import ProductFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filterset_class = ProductFilter
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'created_at']

