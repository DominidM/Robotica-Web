from django.shortcuts import render
import requests

def login_view(request):
    return render(request, 'admin/admin_login.html')

def dashboard_home(request):
    return render(request, 'admin/dashboard_home.html')

def usuarios_list(request):
    return render(request, 'admin/dashboard_usuarios.html')

def sesiones_list(request):
    return render(request, 'admin/dashboard_sesiones.html')

def roles_list(request):
    api_url = "http://127.0.0.1:8001/roles/"  # Cambia si tu API va en otro lado
    print("Consultando API de roles en", api_url)
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        roles = response.json()
        print("Respuesta de roles:", roles)
    except Exception as e:
        roles = []
        print("Error consultando API de roles:", e)
    return render(request, 'admin/dashboard_roles.html', {"roles": roles})

def robots_list(request):
    return render(request, 'admin/dashboard_robots.html')

def emparejamiento_list(request):
    return render(request, 'admin/dashboard_emparejamiento.html')

def emociones_list(request):
    return render(request, 'admin/dashboard_emociones.html')

def mensajes_list(request):
    return render(request, 'admin/dashboard_mensajes.html')