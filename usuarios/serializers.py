from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

Usuario = get_user_model()

class UsuarioCadastroSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id','username','email','senha','first_name','last_name','telefone']

    def create(self, dados_validos):
        usuario = Usuario.objects.create_user(
            username=dados_validos['username'],
            email=dados_validos['email'],
            password=dados_validos['senha'],
            first_name=dados_validos.get['first_name', ''],
            last_name=dados_validos.get['last_name', ''],
            telefone=dados_validos.get['telefone', ''],
        )
        return usuario
    
class MeuTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, usuario):
        token = super().get_token(usuario)

        token['nome'] = usuario.first_name
        token['email'] = usuario.email

        return token