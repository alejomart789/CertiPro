from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    actualizacion = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Pregunta(models.Model):
    TIPOS_PREGUNTA = (
        ('text', 'Texto'),
        ('number', 'Número'),
        ('radio', 'Opción única (Radio)'),
        ('checkbox', 'Casilla de verificación (Checkbox)'),
        ('color', 'Color'),
        ('date', 'Fecha'),
        ('datetime-local', 'Fecha y hora local'),
        ('email', 'Email'),
        ('file', 'Archivo'),
        ('month', 'Mes'),
        ('range', 'Rango'),
        ('tel', 'Teléfono'),
        ('time', 'Hora'),
        ('url', 'URL'),
        ('week', 'Semana'),
        # Agrega más opciones aquí según tus necesidades
    )

    pregunta = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPOS_PREGUNTA)

    def __str__(self):
        return self.pregunta