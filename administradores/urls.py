from django.urls import path
from . import views

app_name = 'administradores'

urlpatterns = [
    path('login/', views.administrador_login, name='administrador_login'),
    # Agrega aquí más URLs para las demás funcionalidades del administrador
    
    path('inicio/<str:usuario>/', views.administrador_inicio, name='administrador_inicio'),  # Asegúrate de tener el mismo nombre aquí
    
    path('actualizacion/', views.actualizacion, name='actualizacion'),
    
    
    path('agregar_pregunta/', views.agregar_pregunta, name='agregar_pregunta'),
    path('editar_pregunta/<int:pk>/', views.editar_pregunta, name='editar_pregunta'),

    path('borrar_pregunta/<int:pk>/', views.borrar_pregunta, name='borrar_pregunta'),
]
