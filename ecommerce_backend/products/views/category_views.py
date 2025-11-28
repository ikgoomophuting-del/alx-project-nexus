# products/views/category_views.py
from rest_framework import generics
from products.models.category import Category
from products.serializers.category_serializer import CategorySerializer
from users.permissions.roles_permissions import IsAdminOrReadOnly


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
