from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='admin_login'),
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('dashboard/usuarios/', views.usuarios_list, name='dashboard_usuarios'),
    path('dashboard/sesiones/', views.sesiones_list, name='dashboard_sesiones'),
    path('dashboard/roles/', views.roles_list, name='dashboard_roles'),
    path('dashboard/robots/', views.robots_list, name='dashboard_robots'),
    path('dashboard/emparejamiento/', views.emparejamiento_list, name='dashboard_emparejamiento'),
    path('dashboard/emociones/', views.emociones_list, name='dashboard_emociones'),
    path('dashboard/mensajes/', views.mensajes_list, name='dashboard_mensajes'),
    path('dashboard/logout/', views.dashboard_logout, name='dashboard_logout'),
]