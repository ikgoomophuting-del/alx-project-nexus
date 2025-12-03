from django.urls import path
from products.views.product_views import ProductListCreateView, ProductDetailView
from products.views.category_views import CategoryListCreateView, CategoryDetailView
from products.views.review_views import ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("reviews/", ReviewListCreateView.as_view(), name="review-list"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
]
