from django_filters import rest_framework as filters
from products.models import Product


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    category = filters.CharFilter(field_name="category__name", lookup_expr="icontains")
    in_stock = filters.BooleanFilter(field_name="is_available")

    class Meta:
        model = Product
        fields = ["min_price", "max_price", "category", "in_stock"]
