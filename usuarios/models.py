from django.db import models
from django.contrib.auth.models import User

from administradores.models import Pregunta

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Update(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Otros campos para almacenar la actualización del usuario
    # ...

    def __str__(self):
        return f"Actualización de {self.user.username} - {self.timestamp}"

class Respuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_texto = models.CharField(max_length=255, blank=True, null=True)
    # Agrega más campos para otros tipos de respuestas según tus necesidades

    def __str__(self):
        return f"Usuario: {self.usuario}, Pregunta: {self.pregunta}, Respuesta: {self.respuesta_texto}"