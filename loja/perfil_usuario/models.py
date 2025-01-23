from django.db import models
from django.contrib.auth.models import User 

class Perfil_usuario(models.Model):
    usuario = models.OneToOneField(User, related_name='perfil_usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.usuario.perfil_usuario
    