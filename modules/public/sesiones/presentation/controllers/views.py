from django.shortcuts import render

def detalle_sesion(request):
    return render(request, 'sesiones/detalle.html')