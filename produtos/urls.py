from django.urls import path
from .views import ListaCriacaoProdutoView, DetalheProdutoView

urlpatterns = [
    path('', ListaCriacaoProdutoView.as_view(), name='lista_criacao_poduto'),
    path('<int:pk>', DetalheProdutoView.as_view, name ='detalhe_produto'),
]
