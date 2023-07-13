from django.urls import path
from usuarios import views

urlpatterns = [
    path('login/', views.usuarioLogin, name='usuario_login'),
    
    path('inicio/<str:usuario>/', views.usuarioInicio, name='usuario_inicio')
]
