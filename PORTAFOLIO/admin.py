from django.contrib import admin

# Register your models here.
from PORTAFOLIO.models import *


class MenuAdmin(admin.ModelAdmin):
    list_display_links = listMenu
    list_display = listMenu
admin.site.register(Menu, MenuAdmin)



class ImagenFilterAdmin(admin.ModelAdmin):
    list_display_links = listImagenFilter
    list_display = listImagenFilter
admin.site.register(ImagenFilter, ImagenFilterAdmin)



class Galery_ProyectAdmin(admin.ModelAdmin):
    list_display_links = listGalery_Proyect
    list_display = listGalery_Proyect
admin.site.register(Galery_Proyect,Galery_ProyectAdmin)


class ProyectoVideoAdmin(admin.ModelAdmin):
    list_display_links = listProyectoVideo
    list_display = listProyectoVideo
admin.site.register(ProyectoVideo, ProyectoVideoAdmin)