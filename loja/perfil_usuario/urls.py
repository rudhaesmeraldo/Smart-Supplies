from django.urls import path
from perfil_usuario import views

urlpatterns = [
    path('fornecedores/<int:pk>/', views.detalhes_fornecedor, name='detalhes_fornecedor'),


]