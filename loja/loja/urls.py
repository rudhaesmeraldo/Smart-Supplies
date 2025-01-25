from django.contrib import admin
from django.urls import path, include
from core.views import frontpage,sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', sobre, name = 'sobre'),
    path('', include('loja_produtos.urls')),
    path('', frontpage, name = 'frontpage'),
]
