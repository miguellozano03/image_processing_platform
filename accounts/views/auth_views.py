from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

class LoginView(TokenObtainPairView):
    pass

class RefreshView(TokenRefreshView):
    pass

class LogoutView(TokenBlacklistView):
    pass