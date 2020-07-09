from django.db import models

# Create your models here.



listCategory_blog=['category']
class Category_blog(models.Model):
    category = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "1. Category"

listBlog=['image','date','title','article','author','status','orden']
class Blog(models.Model):
    category = models.ForeignKey(Category_blog, on_delete=models.CASCADE, null=True, blank=True)
    image=models.FileField(upload_to='index/blog',help_text='imagen de 1200*752')
    date=models.DateField()
    title=models.TextField()
    article=models.TextField()
    author=models.TextField()
    status = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.category.category

    def save(self, force_insert=False, force_update=False, using=None,  update_fields=None):
        cuenta = Blog.objects.count()
        if self.orden == 0:
            self.orden = cuenta + 1
        super(Blog, self).save()

    class Meta:

        verbose_name_plural = "2. blog"

listVisitas_Blog=['blog','visita']
class Visitas_Blog(models.Model):
    blog=models.OneToOneField(Blog, on_delete=models.CASCADE ,null=True,blank=True)
    visita=models.IntegerField(default=1)

    def visitar(self):
        return "<a target='blank' href='http://www.dwindowsdesigns.com/blog/%s'>Ver en la Web</a>" % self.blog.id

    visitar.allow_tags = True
    visitar.short_description = "Ir"

    def save(self, *args, **kwargs):

        self.visita += 1
        super(Visitas_Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "3. Visits in Blog"

# class Comment (models.Model):
#     blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
#     question=models.TextField()
#     user=models.TextField()
#     date=models.DateTimeField(auto_now_add=True)
#     email=models.EmailField()
#
#     def __str__(self):
#
#         return self.question