from django.urls import path
from accounts.views.auth_views import LoginView, RefreshView, LogoutView

urlpatterns = [

    #Auth 
    path('auth/logout',LogoutView.as_view(), name='logout' ),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/refresh', RefreshView.as_view(), name='refresh'),

    #User / Profile

]