from django.db import models

# Create your models here.
listSlider = ['imagen','status','orden']
class Slider(models.Model):
    imagen = models.ImageField(upload_to='index/slider', help_text='Imagen de 900x900')
    status = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        cuenta = Slider.objects.count()
        if self.orden == 0:
            self.orden = cuenta + 1
        super(Slider, self).save()

    class Meta:
        verbose_name_plural = "1. Slider"


listBoxItems = ['icono','titulo','parrafo']
class BoxItem(models.Model):
    icono = models.ImageField(upload_to='index/icon', help_text='Imagen de 60x60')
    titulo = models.CharField(max_length=100)
    parrafo = models.TextField()

    class Meta:
        verbose_name_plural = "2. Box Item"


listFeature = ['imagen','titulo']
class Feature(models.Model):
    imagen = models.ImageField(upload_to='index/features', help_text='Imagen de 960x683')
    titulo = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "3. Feature "

listRecentWorke = ['imagen','titulo','descripcion', 'status','orden']
class RecentWork(models.Model):
    imagen = models.ImageField(upload_to='index/works', help_text='Imagen de 800x650')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    status = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        cuenta = RecentWork.objects.count()
        if self.orden == 0:
            self.orden = cuenta + 1
        super(RecentWork, self).save()



listBlogPost = ['imagen','titulo','descripcion','autor','fecha', 'status','orden']
class BlogPost(models.Model):
    imagen = models.ImageField(upload_to='index/blog', help_text='Imagen de 900x650')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField()
    status = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)


listFooter = ['logo','descripcion']
class Footer(models.Model):
    logo = models.ImageField(upload_to='index/Logo', help_text='Imagen de 113x28')
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = "4. Footer"


listRedesSociales = ['icono','url']
class RedesSociales(models.Model):
    icono = models.CharField(max_length=100,choices=(
        ('fa fa-user','User'),
    ))
    url = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "5. Social networks "

