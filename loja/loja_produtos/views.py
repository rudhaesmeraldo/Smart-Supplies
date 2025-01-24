from django.shortcuts import render, get_object_or_404
from loja_produtos.models import Produto, Categoria


def detalhes_categorias(request,slug):
    return render(request, 'loja_produtos/detalhes_categorias.html')

def detalhes_produtos(request, slug):
    produto = get_object_or_404(Produto, slug=slug)
    return render(request, 'loja_produtos/detalhes_produtos.html',{'produto':produto})