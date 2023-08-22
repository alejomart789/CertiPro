from collections import UserDict
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from administradores import models
from administradores.models import Administrador
from administradores.models import Pregunta
from .forms import PreguntaForm




def administrador_login(request):
    if request.method == 'POST':
        identificacion = request.POST.get('identificacion')
        password = request.POST.get('password')
        user = authenticate(request, username=identificacion, password=password)

        if user is not None and user.administrador:
            login(request, user)
            return redirect('administradores:administrador_inicio', usuario=user.username)
        else:
            messages.error(request, 'Identificación o contraseña incorrecta.')

    return render(request, "administradores/login.html")


def administrador_inicio(request, usuario):
    usuario = request.user
    
    # Obtener el objeto Administrador asociado al usuario actual
    try:
        administrador = Administrador.objects.get(user=request.user)
    except Administrador.DoesNotExist:
        administrador = None
    
    preguntas = Pregunta.objects.all()
    
    # Obtener los tipos de preguntas disponibles
    tipos_pregunta = Pregunta.TIPOS_PREGUNTA
    
    context = {
            'usuario': usuario, 
            'administrador': administrador,
            'preguntas': preguntas,
            'tipos_pregunta': tipos_pregunta,
            }
    return render(request, "administradores/index.html", context)






@csrf_exempt
def actualizacion(request):
    if request.method == 'POST':
        activada = request.POST.get('activada')
        
        if activada == "on":
            activada = True
        else:
            activada = False
        
        try:
            administrador = Administrador.objects.get(user=request.user)
            administrador.actualizacion = activada
            administrador.save()
            return redirect('administrador_inicio', usuario=request.user.username)
        except Administrador.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'No se encontró el registro del Administrador'}, status=400)

    # Si la solicitud no es POST, retornamos un error
    return JsonResponse({'success': False, 'error': 'Solicitud inválida'}, status=400)

def agregar_pregunta(request):
    form = PreguntaForm()

    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            pregunta = form.save()
            # Devolver una respuesta JSON con un mensaje de éxito y la pregunta recién agregada
            return JsonResponse({'success': True, 'pregunta': pregunta.pregunta})
        else:
            # Devolver una respuesta JSON con los errores del formulario
            return JsonResponse({'success': False, 'errors': form.errors})
    
    context = {'form': form}
    
    if request.is_ajax():
        return render(request, "administradores/modal_agregar_pregunta.html", context)
    else:
        return render(request, "administradores/index.html", context)

def editar_pregunta(request):
    if request.method == 'POST':
        pregunta_id = request.POST.get('preguntaId')
        pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return JsonResponse({'success': False, 'message': 'Método no válido'})

def borrar_pregunta(request, pk):
    pregunta = get_object_or_404(Pregunta, pk=pk)
    if request.method == 'POST':
        pregunta.delete()
        return redirect('administradores:administrador_inicio')
    return render(request, 'administradores/borrar_pregunta_confirm.html', {'pregunta': pregunta})