from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='public_home'),  # /public/home
    # Puedes agregar más rutas públicas aquí
]