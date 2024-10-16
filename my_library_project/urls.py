from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('library.urls')),  # Inclui as URLs da biblioteca
    path('auth/', include('rest_framework.urls')),  # Para a autenticação básica
]
