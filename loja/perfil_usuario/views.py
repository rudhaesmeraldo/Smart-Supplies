from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from perfil_usuario.models import Perfil_usuario

def detalhes_fornecedor(request, pk):
    usuario = User.objects.get(pk=pk)

    return render(request,'perfil_usuario/detalhes_fornecedor.html',{'usuario':usuario})

def cadastrar(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()

            login(request, usuario)
            perfil_usuario = Perfil_usuario.objects.create(usuario=usuario)

            return redirect('frontpage')
    
    else:
        formulario = UserCreationForm()

    return render(request,'perfil_usuario/cadastrar.html',{'formulario':formulario})