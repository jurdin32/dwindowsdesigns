from django.contrib import admin

# Register your models here.
from PRODUCTO.models import *


class CategoriaAdmin(admin.ModelAdmin):
    list_display_links = listCategoria
    list_display = listCategoria
admin.site.register(Categoria, CategoriaAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display_links = listProducto
    list_display = listProducto
admin.site.register(Producto, ProductoAdmin)

class Galeria_ProductoAdmin(admin.ModelAdmin):
    list_display_links = listGaleria_Producto
    list_display = listGaleria_Producto
admin.site.register(Galeria_Producto,Galeria_ProductoAdmin)