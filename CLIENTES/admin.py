from django.contrib import admin

# Register your models here.
import CLIENTES

from CLIENTES.models import listClientes, Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display_links = listClientes
    list_display = listClientes
admin.site.register(Cliente, ClienteAdmin)