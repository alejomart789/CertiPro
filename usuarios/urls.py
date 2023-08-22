from django.urls import path
from usuarios import views

urlpatterns = [
    path('login/', views.usuarioLogin, name='usuario_login'),
    
    path('inicio/<str:usuario>/', views.usuarioInicio, name='usuario_inicio'),
    
    path('responder_preguntas/', views.responder_preguntas, name='responder_preguntas'),
    path('ver_respuestas/', views.ver_respuestas, name='ver_respuestas'),
]
