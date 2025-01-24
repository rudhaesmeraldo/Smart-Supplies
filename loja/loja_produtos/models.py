from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.titulo

class Produto(models.Model):
    usuario = models.ForeignKey(User, related_name='produto', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    descricao = models.TextField(blank=True)
    preco = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    def display_preco(self):
        return self.preco/100
     
    class Meta:
        ordering = ('-criado_em',)
        verbose_name_plural = 'Produtos'