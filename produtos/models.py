from django.db import models
from fornecedores.models import Fornecedor

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='produtos')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome