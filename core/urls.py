from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_home, name='public_home'),  # /public/
    path('about/', views.public_about, name='public_about'),  # /public/about/
    # ...otros endpoints públicos
]