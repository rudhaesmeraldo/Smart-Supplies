from django.contrib import admin
from django.urls import path, include
from core.views import frontpage,sobre

urlpatterns = [
    path('', include('loja_produtos.urls')),
    path('admin/', admin.site.urls),
    path('', frontpage, name = 'frontpage'),
    path('sobre/', sobre, name = 'sobre'),
]
