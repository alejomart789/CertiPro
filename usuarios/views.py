from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def usuarioLogin(request):
    if request.method == 'POST':
        identificacion = request.POST.get('identificacion')
        password = request.POST.get('password')
        user = authenticate(request, username=identificacion, password=password)
        if user is not None:
            login(request, user)
            return redirect('usuario_inicio', usuario = request.user.username)
        else:
            messages.error(request, 'Identificación o contraseña incorrecta.')
    
    return render(request, "usuarios/login.html")

def usuarioInicio(request, usuario):
    
    usuario = request.user
    
    return render(request, "usuarios/index.html", {'usuario': usuario})
