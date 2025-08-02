from django.urls import path
from modules.public.sesiones.presentation.controllers import views

urlpatterns = [
    path('detalle/', views.detalle_sesion, name='detalle_sesion'),
]