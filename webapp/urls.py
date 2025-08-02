from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Para el home
    path('sesiones/', include('modules.public.sesiones.routes.urls')),  # Para sesiones
]