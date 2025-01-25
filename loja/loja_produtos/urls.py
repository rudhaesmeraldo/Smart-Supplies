from django.urls import path
from loja_produtos import views

urlpatterns = [
    path('<slug:slug>/', views.detalhes_categorias, name='detalhes_categorias'),
    path('<slug:categoria_slug>/<slug:slug>/', views.detalhes_produtos, name='detalhes_produtos'),
]
