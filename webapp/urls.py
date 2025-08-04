from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Home
    path('sesiones/', include('modules.public.sesiones.routes.urls')),
    path('public/', include('modules.public.urls')),  # Todo lo de /public/
    path('adminroutes/', include('modules.adminroutes.urls')),  # Todo lo de /adminroutes/
]