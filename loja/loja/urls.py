from django.contrib import admin
from django.urls import path, include
from core.views import frontpage,sobre
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sobre/', sobre, name = 'sobre'),
    path('admin/', admin.site.urls),
    path('', include('perfil_usuario.urls')),
    path('', include('loja_produtos.urls')),
    path('', frontpage, name = 'frontpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
