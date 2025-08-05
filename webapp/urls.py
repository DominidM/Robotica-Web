from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('public/', include('modules.routes.public.urls')),
    path('adminpanel/', include('modules.routes.adminpanel.urls')),
    path('', RedirectView.as_view(url='/public/home', permanent=False)),  # <--- Esta línea
    # path('admin/', admin.site.urls),  # deja esto si quieres el admin nativo, si no, quítalo
]