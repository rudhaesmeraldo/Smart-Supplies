from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome