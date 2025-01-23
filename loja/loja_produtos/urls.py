from django.urls import path
from loja_produtos import views

urlpatterns = [
    path('<slug:slug>/', views.detalhes_categoria, name='detalhes_categoria'),
    path('<slug:slug>/', views.detalhes_produtos, name='detalhes_produtos'),
]
