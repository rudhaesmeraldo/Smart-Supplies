from django.contrib import admin
from django.urls import path, include
from core.views import frontpage,sobre
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', sobre, name = 'sobre'),
    path('', include('loja_produtos.urls')),
    path('', frontpage, name = 'frontpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
