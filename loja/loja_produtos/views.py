from django.shortcuts import render, get_object_or_404
from loja_produtos.models import Produto


def detalhes_categoria(request,slug):
    return render(request, 'loja_produtos/detalhes_categoria.html')

def detalhes_produtos(request, slug):
    produto = get_object_or_404(Produto, slug=slug)
    return render(request, 'loja_produtos/detalhes_produtos.html',{'produto':produto})