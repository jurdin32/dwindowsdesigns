from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from PRINCIPAL.views import index
from PORTAFOLIO import views as portafolio_views
from EMPRESA import views as empresa_views
from PRODUCTO import views as producto_views
from BLOG import views as blog_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('',index, name='index'),
    path('acercade/', empresa_views.AntecedentesView, name='acercade'),
    path('portafolio/', portafolio_views.PortafolioView, name='portafolio'),
    path('portafolio/foto/<int:id>/', portafolio_views.PortafolioFotoView, name='portafolioFoto'),
    path('producto/foto/<int:idCategoria>/', producto_views.ProductoView, name="product"),
    path('blog/<int:id>/', blog_views.BlogView, name='blog_list'),
    path('blog/post/<int:n>/', blog_views.BlogPostView, name='blog_post'),
    path('contacto/', empresa_views.ContactoView, name='contacto'),
    path('services/', empresa_views.ServicesView, name='services'),

]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
admin.site.site_header = 'WINDOWS DESIGNS'