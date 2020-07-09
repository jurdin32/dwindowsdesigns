from django.contrib import admin

# Register your models here.
from EMPRESA.models import *


class AntecedentesAdmin(admin.ModelAdmin):
    list_display_links = listAntecedentes
    list_display = listAntecedentes
admin.site.register(Antecedentes, AntecedentesAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = listCompany
    list_display_links = listCompany
admin.site.register(Company,CompanyAdmin)

class CompanyLogoAdmin(admin.ModelAdmin):
    list_display = listCompanyLogo
    list_display_links = listCompanyLogo
admin.site.register(CompanyLogo,CompanyLogoAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = listContact
    list_display_links = listContact
admin.site.register(Contact,ContactAdmin)

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = listProveedores
    list_display_links = listProveedores
admin.site.register(Proveedores, ProveedoresAdmin)

class ServicesAdmin(admin.ModelAdmin):
    list_display = listServices
    list_display_links = listServices
admin.site.register(Services, ServicesAdmin)