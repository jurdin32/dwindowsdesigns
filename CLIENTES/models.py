from django.db import models

# Create your models here.

listClientes = ['identificacion','nombres','apellidos','direccion','telefono','convencional','email','estado']
class Cliente(models.Model):
    identificacion = models.CharField(max_length=13, unique=True)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    convencional = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    imagen = models.ImageField(upload_to='Clientes', null=True, blank=True)
    estado = models.BooleanField(default=True)