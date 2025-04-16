from django.urls import path
from .views import ListaCriacaoFornecedorView, DetalheFornecedorView

urlpatterns = [
    path('', ListaCriacaoFornecedorView.as_view(), name='lista_criacao_fornecedor'),
    path('<int:pk>/', DetalheFornecedorView.as_view(), name='detalhe_fornecedor'),
]
