from django.shortcuts import render

# Create your views here.
from EMPRESA.models import *
from PRINCIPAL.models import *
from PRODUCTO.models import *


def ProductoView(request, idCategoria):
    logo = CompanyLogo.objects.get()
    footer = Footer.objects.all()
    rsociales = RedesSociales.objects.all()
    contact = Contact.objects.get()
    category = Categoria.objects.all()
    product = Producto.objects.filter(categoria=idCategoria)[0:4]
    galerias = Galeria_Producto.objects.all()
    proveedores = Proveedores.objects.all()

    contexto = {

        'proveedores': proveedores,
        'galerias':galerias,
        'product':product,
        'logo': logo,
        'footers': footer,
        'categoria': category,
        'contact': contact,
        'rsociales': rsociales,
    }
    return render(request, 'product.html',contexto)

