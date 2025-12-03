from rest_framework import serializers
from products.models.product import Product
from products.models.category import Category
from products.models.review import Review


# -------------------- CATEGORY SERIALIZER --------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "description"]


# -------------------- REVIEW SERIALIZER --------------------
class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.ReadOnlyField(source='reviewer.email')

    class Meta:
        model = Review
        fields = [
            "id",
            "reviewer",
            "rating",
            "comment",
            "created_at",
        ]


# -------------------- PRODUCT SERIALIZER --------------------
class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(
        write_only=True,
        required=False,
        allow_null=True
    )
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "price",
            "stock",
            "is_available",
            "category",
            "category_id",
            "owner",
            "reviews",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["slug", "owner"]

    def create(self, validated_data):
        category_id = validated_data.pop("category_id", None)
        if category_id:
            validated_data["category"] = Category.objects.get(pk=category_id)
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        category_id = validated_data.pop("category_id", None)
        if category_id is not None:
            instance.category = Category.objects.get(pk=category_id)
        return super().update(instance, validated_data)
