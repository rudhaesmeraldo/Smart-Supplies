from django import template
from loja_produtos.models import Categoria


registrar = template.Library()

@registrar.inclusion_tag('core/menu.html')
def menu():
    categorias = Categoria.objects.all()
    return{
        'categorias':categorias
    }