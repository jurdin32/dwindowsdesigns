from django.contrib import admin

# Register your models here.
from BLOG.models import *


class BlogAdmin(admin.ModelAdmin):
    list_display_links = listBlog
    list_display = listBlog
admin.site.register(Blog, BlogAdmin)

class Category_blogAdmin(admin.ModelAdmin):
    list_display_links = listCategory_blog
    list_display = listCategory_blog
admin.site.register(Category_blog, Category_blogAdmin)

class Visitas_BlogAdmin(admin.ModelAdmin):
    list_display_links = listVisitas_Blog
    list_display = listVisitas_Blog
admin.site.register(Visitas_Blog, Visitas_BlogAdmin)