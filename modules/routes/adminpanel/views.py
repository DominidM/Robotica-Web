from django.shortcuts import render
from django.contrib.auth import logout  # <-- Import logout correctly!
import requests

def login_view(request):
    return render(request, 'admin/admin_login.html')

def dashboard_home(request):
    return render(request, 'admin/dashboard_home.html')

def usuarios_list(request):
    api_url = "http://127.0.0.1:8001/api/usuarios/"
    print("Consultando API de usuarios en", api_url)
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        usuarios = response.json()
        print("Respuesta de usuarios:", usuarios)
    except Exception as e:
        usuarios = []
        print("Error consultando API de usuarios:", e)
    return render(request, 'admin/dashboard_usuarios.html', {"usuarios": usuarios})

def dashboard_logout(request):
    logout(request)  # <-- Correct use after importing!
    return render(request, 'admin/dashboard_logout.html')

def sesiones_list(request):
    api_url = "http://127.0.0.1:8001/api/sesiones/"
    print("Consultando API de sesiones en", api_url)
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        sesiones = response.json()
        print("Respuesta de sesiones:", sesiones)
    except Exception as e:
        sesiones = []
        print("Error consultando API de sesiones:", e)
    return render(request, 'admin/dashboard_sesiones.html', {"sesiones": sesiones})

def roles_list(request):
    api_url = "http://127.0.0.1:8001/api/roles/"
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
    api_url = "http://127.0.0.1:8001/api/robots/"
    print("Consultando API de robots en", api_url)
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        robots = response.json()
        print("Respuesta de robots:", robots)
    except Exception as e:
        robots = []
        print("Error consultando API de robots:", e)
    return render(request, 'admin/dashboard_robots.html', {"robots": robots})

def emparejamiento_list(request):
    api_url = "http://127.0.0.1:8001/api/emparejamientos/"
    print("Consultando API de emparejamientos en", api_url)
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        emparejamientos = response.json()
        print("Respuesta de emparejamientos:", emparejamientos)
    except Exception as e:
        emparejamientos = []
        print("Error consultando API de emparejamientos:", e)
    return render(request, 'admin/dashboard_emparejamiento.html', {"emparejamientos": emparejamientos})

def emociones_list(request):
    api_url = "http://127.0.0.1:8001/api/emociones/"
    print("Consultando API de emociones en", api_url)
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        emociones = response.json()
        print("Respuesta de emociones:", emociones)
    except Exception as e:
        emociones = []
        print("Error consultando API de emociones:", e)
    return render(request, 'admin/dashboard_emociones.html', {"emociones": emociones})

def mensajes_list(request):
    api_url = "http://127.0.0.1:8001/api/mensajes/"
    print("Consultando API de mensajes en", api_url)
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        mensajes = response.json()
        print("Respuesta de mensajes:", mensajes)
    except Exception as e:
        mensajes = []
        print("Error consultando API de mensajes:", e)
    return render(request, 'admin/dashboard_mensajes.html', {"mensajes": mensajes})