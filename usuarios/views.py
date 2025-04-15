from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UsuarioCadastroSerializer, MeuTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

Usuario = get_user_model()

# Cadastro
class CadastroUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioCadastroSerializer

# Login com JWt
class LoginJWTView(TokenObtainPairView):
    serializer_class = MeuTokenSerializer