from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
from BLOG.models import *
from EMPRESA.models import *
from PRINCIPAL.models import *
from PRODUCTO.models import *


def BlogView(request, id):

    if id == 0:
        blogPag = Blog.objects.filter(status=True).order_by('-orden')

    else:
        blogPag = Blog.objects.filter(category=id).order_by('-orden')

    paginator = Paginator(blogPag, 3)
    page = request.GET.get('page')
    blog_pag = paginator.get_page(page)

    logo = CompanyLogo.objects.get()
    category_menu = Categoria.objects.all()
    footer = Footer.objects.all()
    rsociales = RedesSociales.objects.all()
    contact = Contact.objects.get()
    category = Category_blog.objects.all()


    contexto = {
        'logo': logo,
        'categoria': category_menu,
        'footers': footer,
        'rsociales': rsociales,
        'contact': contact,
        'category':category,
        'visitas': Visitas_Blog.objects.all(),

        'blog_pag':blog_pag
    }
    return render(request, 'blog-list.html', contexto)

def BlogPostView(request,n):
    logo = CompanyLogo.objects.get()
    category = Categoria.objects.all()
    footer = Footer.objects.all()
    rsociales = RedesSociales.objects.all()
    contact = Contact.objects.get()
    blog_list = Blog.objects.all()
    try:
        Visitas_Blog(blog_id=n).save()
    except:
        visita=Visitas_Blog.objects.get(blog_id=n)
        visita.save()
    blog = Blog.objects.filter(id=n)
    category_blog = Category_blog.objects.all()
    contexto = {
        'logo': logo,
        'categoria': category,
        'footers': footer,
        'rsociales': rsociales,
        'contact': contact,
        'blog':blog,
        'category_blog': category_blog,
        'blog_list':blog_list
    }
    return render(request, 'blog-post.html', contexto)

