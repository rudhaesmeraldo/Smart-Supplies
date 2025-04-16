from rest_framework import generics, permissions
from .models import Fornecedor
from .serializers import FornecedorSerializer

# listar e criar fornecedores 
class ListaCriacaoFornecedorView(generics.ListCreateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    permission_classes = [permissions.IsAuthenticated]

# ver, atualizar e deletar um fornecedor específico
class DetalheFornecedorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    permission_classes = [permissions.IsAuthenticated]
    