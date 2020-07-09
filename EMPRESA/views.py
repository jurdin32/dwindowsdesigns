from django.core.paginator import Paginator
from django.shortcuts import render
from django.conf import settings

from EMPRESA.emailes import send_email
from EMPRESA.models import *
from PRINCIPAL.models import *
from PRODUCTO.models import *


def AntecedentesView(request):
    company = Company.objects.get()
    companylogo = CompanyLogo.objects.all()
    antecedente = Antecedentes.objects.all()
    box = BoxItem.objects.all()
    seccion = SeccionFoto.objects.all()
    proveedores = Proveedores.objects.all()
    category = Categoria.objects.all()
    footer = Footer.objects.all()
    rsociales = RedesSociales.objects.all()
    contact = Contact.objects.get()
    logo = CompanyLogo.objects.get()
    producto = Producto.objects.all()

    contexto = {
        'logo':logo,
        'company': company,
        'companylogo': companylogo,
        'antecedentes': antecedente,
        'boxs': box,
        'secciones': seccion,
        'proveedores': proveedores,
        'categoria': category,
        'footers': footer,
        'rsociales': rsociales,
        'contact': contact,
        'producto': producto,
    }
    return render(request, 'acercade.html', contexto)


def ContactoView(request):
    if request.method == 'POST':
       print(request.POST)
       name = request.POST['name']
       phone = request.POST['phone']
       email = request.POST['email']
       comment = request.POST['comment']
       send_email("Mesage this web",comment,name+" | "+phone+"<"+email+">",['dolores@dwindowsdesigns.com'])

    logo = CompanyLogo.objects.get()
    footer = Footer.objects.all()
    rsociales = RedesSociales.objects.all()
    box = BoxItem.objects.all()
    category = Categoria.objects.all()
    producto = Producto.objects.all()
    contact = Contact.objects.get()
    contexto = {
        'logo':logo,
        'footers': footer,
        'rsociales': rsociales,
        'contact': contact,
        'boxs': box,
        'categoria': category,
        'producto': producto,
    }
    return render(request, 'contacto.html', contexto)


def ServicesView(request):
    services = Services.objects.all()
    paginator = Paginator(services, 3)
    page = request.GET.get('page')
    service = paginator.get_page(page)

    logo = CompanyLogo.objects.get()
    rsociales = RedesSociales.objects.all()
    contact = Contact.objects.get()
    footer = Footer.objects.all()
    category = Categoria.objects.all()

    contexto = {
        'logo': logo,
        'footers': footer,
        'categoria': category,
        'contact': contact,
        'rsociales': rsociales,
        'services': service
    }
    return render(request, 'services.html', contexto)