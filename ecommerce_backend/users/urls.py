from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views.auth_views import RegisterView, LoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("login/", LoginView.as_view(), name="login"),
    path("", CategoryListView.as_view()),
    path("<int:pk>/", CategoryDetailView.as_view()),
    path("", ProductListView.as_view()),
    path("<int:pk>/", ProductDetailView.as_view()),
    path("profile/", UserProfileView.as_view()),
]
