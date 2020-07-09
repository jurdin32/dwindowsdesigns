from django.shortcuts import render

# Create your views here.
from BLOG.models import *
from EMPRESA.models import *
from PORTAFOLIO.models import *
from PRINCIPAL.models import *
from PRODUCTO.models import *


def index(request):
    slider = Slider.objects.filter(status=True).order_by('-orden')
    boxItem = BoxItem.objects.all()
    feature = Feature.objects.all()
    footer = Footer.objects.all()
    logo = CompanyLogo.objects.get()
    rsociales = RedesSociales.objects.all()
    contact = Contact.objects.get()
    category = Categoria.objects.all()
    project = ImagenFilter.objects.filter(status=True).order_by('-orden')[0:3]
    blogs = Blog.objects.filter(status=True).order_by('-date')[0:3]


    contexto = {
        'sliders': slider,
        'logo': logo,
        'boxs': boxItem,
        'features': feature,
        'footers': footer,
        'rsociales': rsociales,
        'contact': contact,
        'categoria': category,
        'projects': project,
        'blogs': blogs,
        'visitas': Visitas_Blog.objects.all(),
    }
    return render(request, 'index.html', contexto)
