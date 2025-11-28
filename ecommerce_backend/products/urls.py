from rest_framework.routers import DefaultRouter
from products.views.product_views import ProductViewSet
from products.views.category_views import CategoryViewSet
from products.views.review_views import ReviewViewSet  # if you have this

router = DefaultRouter()

router.register(r"products", ProductViewSet, basename="products")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"reviews", ReviewViewSet, basename="reviews")

urlpatterns = router.urls
