from django.contrib import admin
from django.urls import include, path
from usuarios import views

urlpatterns = [
    path("", views.usuarioLogin, name='Login'),
    path('admin/', admin.site.urls),
    
    path('usuario/', include('usuarios.urls')),
]
