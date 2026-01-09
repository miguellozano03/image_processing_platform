from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from rest_framework.generics import CreateAPIView

from drf_spectacular.utils import extend_schema, OpenApiResponse

from accounts.models import User
from accounts.serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    @extend_schema(
        description="Register a new user account.",
        responses={
            201: RegisterSerializer,
            400: OpenApiResponse(description="Invalid registration data"),
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class LoginView(TokenObtainPairView):
    pass

class RefreshView(TokenRefreshView):
    pass

class LogoutView(TokenBlacklistView):
    pass
