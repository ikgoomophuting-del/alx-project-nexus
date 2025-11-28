from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"reviews", ReviewViewSet, basename="reviews")
urlpatterns = router.urls
