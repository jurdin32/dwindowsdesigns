from django.db import models

# Create your models here.
listAntecedentes = ['imagen','titulo','parrafo']
class Antecedentes(models.Model):
    imagen = models.ImageField(upload_to='empresa/antecedentes', help_text='Imagen de 960x650')
    titulo = models.CharField(max_length=100)
    parrafo = models.TextField()

    class Meta:
        verbose_name_plural = "1. Antecedentes"


listBoxItems = ['icono','titulo','parrafo']
class BoxItem(models.Model):
    icono = models.CharField(max_length=100,choices=(
        ('icon-desktop','icon-desktop'),
        ('icon-desktop','icon-desktop'),
        ('icon-desktop', 'icon-desktop')
    ))
    titulo = models.CharField(max_length=100)
    parrafo = models.TextField()



listSeccionFoto = ['imagen_1','parrafo','imagen_2','titulo_1','objetivo','titulo_2','mision','titulo_3','vision']
class SeccionFoto(models.Model):
    imagen_1 = models.ImageField(upload_to='empresa/foto_1', help_text='Imagen de 1000x700')
    parrafo = models.TextField(max_length=100,blank=True, null=True)
    imagen_2 = models.ImageField(upload_to='empresa/foto_2', help_text='Imagen de 500x730')
    titulo_1 = models.CharField(max_length=100)
    objetivo = models.TextField(blank=True, null=True)
    titulo_2 = models.CharField(max_length=100,blank=True, null=True)
    mision = models.TextField(blank=True, null=True)
    titulo_3 = models.CharField(max_length=100, blank=True, null=True)
    vision = models.TextField(blank=True, null=True)



# no borrar estoy actualizando los nombres
listCompany=['image_1','title_about','paragraph_about','image_2','image_3','title_1','objetive','title_2','mission','title_3','view']
class Company(models.Model):
    image_1 = models.ImageField(upload_to='company/', help_text='Imagen de 1000x700')
    title_about = models.CharField(max_length=100, blank=True, null=True)
    paragraph_about = models.TextField(max_length=900, blank=True, null=True)
    image_2 = models.ImageField(upload_to='company/', help_text='Imagen de 500x730')
    image_3 = models.ImageField(upload_to='company/', help_text='Imagen de 2500x730')
    title_1 = models.CharField(max_length=100,default='Objetive' ,blank=True, null=True)
    objetive = models.TextField(blank=True, null=True)
    title_2 = models.CharField(max_length=100,default='Mission',blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    title_3 = models.CharField(max_length=100,default='View', blank=True, null=True)
    view = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "2. Company"


listCompanyLogo = ['logo','logo_with_color','logo_white']
class CompanyLogo(models.Model):
    logo = models.ImageField(upload_to='index/Logo' , blank=True, null=True)
    logo_with_color = models.ImageField(upload_to='index/Logo', blank=True, null=True)
    logo_white = models.ImageField(upload_to='index/Logo', blank=True, null=True)
    class Meta:
        verbose_name_plural = "3. Company logo"

listProveedores = ['url','logo']
class Proveedores(models.Model):
    url = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='index/Logo')

    class Meta:
        verbose_name_plural = "4. Provider"



listContact = ['address','street','name','map','email','phone']
class Contact(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    map=models.TextField(max_length=800,null=True,blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "5. Contact"

listServices = ['image','title','description']
class Services(models.Model):
    image = models.ImageField(upload_to='service/', help_text='Imagen de 500x500')
    title = models.CharField(max_length=200)
    description = models.TextField()