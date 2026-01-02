from django.urls import path
from accounts.views.auth_views import (
    RegisterView,
    LoginView,
    RefreshView,
    LogoutView,
)

urlpatterns = [

    #Auth 
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/refresh', RefreshView.as_view(), name='refresh'),
    path('auth/logout',LogoutView.as_view(), name='logout' ),

    #User / Profile

]