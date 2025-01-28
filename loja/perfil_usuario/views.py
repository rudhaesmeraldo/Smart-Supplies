from django.shortcuts import render
from django.contrib.auth.models import User

def detalhes_fornecedor(request, pk):
    usuario = User.objects.get(pk=pk)

    return render(request,'perfil_usuario/detalhes_fornecedor.html',{'usuario':usuario})