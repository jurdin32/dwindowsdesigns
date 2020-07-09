from django.db import models

# Create your models here.

listCategoria = ['nombre', 'descripcion']
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    def __str__(self):

        return self.nombre
    class Meta:
        verbose_name_plural = "1. Categoy"


listProducto = ['categoria','nombre', 'descripcion','portada','image_muestra','marca']
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=400,null=True, blank=True)
    portada= models.ImageField(upload_to='index/producto',help_text="imagen de 1920x1292")
    image_muestra= models.ImageField(upload_to='index/producto',help_text="imagen de 500x500")
    marca=models.CharField(max_length=100,null=True)
    status = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    def __str__(self):

        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        cuenta = Producto.objects.count()
        if self.orden == 0:
            self.orden = cuenta + 1
        super(Producto, self).save()

    class Meta:
        verbose_name_plural = "2. Product"

listGaleria_Producto=['producto','foto']
class Galeria_Producto(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    foto=models.ImageField(upload_to='index/producto',help_text="imagen de 800x650")

    class Meta:
        verbose_name_plural = "3. Galery_Prodcut"