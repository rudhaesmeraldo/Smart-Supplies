from django.shortcuts import render
from loja_produtos.models import Produto

def frontpage(request):
    produtos = Produto.objects.all()[0:6]
    return render(request,'core/frontpage.html',{'produtos': produtos})
    
def sobre(request):
    return render(request,'core/sobre.html')