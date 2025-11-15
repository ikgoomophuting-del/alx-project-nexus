from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views.product_views import ProductViewSet
from products.views.category_views import CategoryViewSet

router = DefaultRouter()
router.register("items", ProductViewSet, basename="products")
router.register("categories", CategoryViewSet, basename="categories")

urlpatterns = router.urls
