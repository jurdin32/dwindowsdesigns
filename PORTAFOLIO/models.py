from django.db import models

from PRODUCTO.models import Categoria

listMenu= ['menu','filtro','descripcion']
class Menu(models.Model):
    menu = models.CharField(max_length=200)
    filtro = models.CharField(max_length=100, choices=(
        ('*', 'Todas'),
        ('.web', 'Sala'),
        ('.advertising', 'cocina'),
        ('.branding', 'Dormitorio'),
        ('.design', 'Baño'),
        ('.photography', 'Comedor'),
    ), null=True, blank=True)
    descripcion = models.CharField(max_length=400)



listImagenFilter= ['category','imagen','titulo','descripcion','status','orden','client','date']
class ImagenFilter(models.Model):
    category=models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True,blank=True)
    imagen = models.ImageField(upload_to='index/portalio', help_text='Imagen de 900x900')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    status = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    client=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField( auto_now=True)

    def __str__(self):

        return self.titulo

    class Meta:
        verbose_name_plural = "1. Project"


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        cuenta = ImagenFilter.objects.count()
        if self.orden == 0:
            self.orden = cuenta + 1
        super(ImagenFilter, self).save()

listGalery_Proyect=['project','photo']
class Galery_Proyect(models.Model):
    project=models.ForeignKey(ImagenFilter,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='index/proyecto',help_text='Imagen de 800x650')
    class Meta:
        verbose_name_plural = "2. Galery Project"

listDetalleFiltro= ['imagen','titulo','descripcion']
class DetalleFiltro(models.Model):
    imagen = models.ImageField(upload_to='index/portalio', help_text='Imagen de 800x514')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen_slider = models.ImageField(upload_to='index/portalio', help_text='Imagen de 1000x673', null=True, blank=True)

listProyectoVideo= ['rutaVideo','descripcion']
class ProyectoVideo(models.Model):
    rutaVideo = models.FileField(upload_to='video/proyectos')
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = "4. Galery video Project"