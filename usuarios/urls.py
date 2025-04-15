from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CadastroUsuarioView, LoginJWTView

urlpatterns = [
    path('cadastro/', CadastroUsuarioView.as_view(), name='cadastro'),
    path('login/', LoginJWTView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
