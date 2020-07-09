from django.contrib import admin

# Register your models here.
from TELAS.models import listTelas, Telas, listCategoriaTela, CategariaTela


class TelasAdmin(admin.ModelAdmin):
    list_display_links = listTelas
    list_display = listTelas
admin.site.register(Telas, TelasAdmin)

class CategoriaTelasAdmin(admin.ModelAdmin):
    list_display_links = listCategoriaTela
    list_display = listCategoriaTela
admin.site.register(CategariaTela, CategoriaTelasAdmin)