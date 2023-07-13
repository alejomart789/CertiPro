from django.db import models
from django.contrib.auth.models import User

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
