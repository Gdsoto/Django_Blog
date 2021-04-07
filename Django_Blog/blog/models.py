from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nombre')
    description = models.CharField(max_length=200, verbose_name='Descripcion')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Creado El')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(
        default='null', verbose_name='Imagen', upload_to='posts')
    public = models.BooleanField(default=True, verbose_name='Publico?')
    user = models.ForeignKey(User, editable=True, verbose_name='Usuario', on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        Tag, verbose_name='Tag', blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
