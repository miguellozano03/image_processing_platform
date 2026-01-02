from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from rest_framework.generics import CreateAPIView

from accounts.models import User
from accounts.serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    pass

class RefreshView(TokenRefreshView):
    pass

class LogoutView(TokenBlacklistView):
    pass
