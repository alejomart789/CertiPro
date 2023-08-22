from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from usuarios.models import Respuesta
from administradores.models import Pregunta

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


def responder_preguntas(request):
    preguntas = Pregunta.objects.all()

    if request.method == 'POST':
        for pregunta in preguntas:
            respuesta_texto = request.POST.get(f"pregunta_{pregunta.id}")

            Respuesta.objects.create(
                usuario=request.user,
                pregunta=pregunta,
                respuesta_texto=respuesta_texto,
            )

    return render(request, 'usuarios/responder_preguntas.html', {'preguntas': preguntas})

def ver_respuestas(request):
    respuestas = Respuesta.objects.filter(usuario=request.user)
    return render(request, 'usuarios/ver_respuestas.html', {'respuestas': respuestas})