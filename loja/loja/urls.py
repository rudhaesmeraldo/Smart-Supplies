from django.contrib import admin
from django.urls import path
from core.views import frontpage,sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name = 'frontpage'),
    path('sobre/', sobre, name = 'sobre'),
]
