from django.db import models

# Create your models here.

listCategoriaTela= ['nombre','descripcion']
class CategariaTela(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)

listTelas = ['nombre','imagen','detalle', 'categoria']
class Telas(models.Model):
    categoria = models.ForeignKey(CategariaTela, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='Telas', null=True, blank=True)
    detalle = models.CharField(max_length=200)