from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserDetailAPIView, UserListApiView

app_name = UsersConfig.name

urlpatterns = [
    path(
        "create_token/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token",
    ),
    path(
        "token/refresh",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token-refresh",
    ),
    path("user/", UserListApiView.as_view(), name="users_list"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("profile/<int:pk>/", UserDetailAPIView.as_view(), name="profile"),
]
