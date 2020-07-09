from django.db.models.fields import return_None
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
from EMPRESA.models import Contact, CompanyLogo
from PORTAFOLIO.models import *
from PRINCIPAL.models import *
from PRODUCTO.models import *


def PortafolioView(request):
    imagen = ImagenFilter.objects.filter(status=True).order_by('-orden')[0:4]
    video = ProyectoVideo.objects.all()
    producto = Producto.objects.all()
    footer = Footer.objects.all()
    rsociales = RedesSociales.objects.all()
    contact = Contact.objects.get()
    logo = CompanyLogo.objects.get()
    categoria=Categoria.objects.all()

    contexto = {

        'imagenes':imagen,
        'videos': video,
        'categoria':categoria,
        'prodcuto':producto,
        'logo': logo,
        'footers': footer,
        'contact': contact,
        'rsociales': rsociales,
    }

    return render(request, 'portafolio.html', contexto)

def PortafolioFotoView(request, id):
    logo = CompanyLogo.objects.get()
    projet_view= ImagenFilter.objects.get(id=id)
    galery_proyect= Galery_Proyect.objects.filter(project=projet_view)
    detalles = DetalleFiltro.objects.all()
    producto = Producto.objects.all()
    footer = Footer.objects.all()
    rsociales = RedesSociales.objects.all()
    contact = Contact.objects.all()
    categoria = Categoria.objects.all()

    contexto ={
        'projet_view':projet_view,
        'galery_proyect': galery_proyect,
        'detalles':detalles,
        'categoria': categoria,
        'contactos': contact,
        'producto':producto,
        'logo': logo,
        'footers': footer,
        'contact': contact,
        'rsociales': rsociales,
    }

    return render(request, 'detalle.html', contexto)