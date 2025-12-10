from rest_framework import serializers
from .models import Product, Category, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name","slug","description"]

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    class Meta:
        model = Review
        fields = ["id","product","user","rating","comment","created_at"]

