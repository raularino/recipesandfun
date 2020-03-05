from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class recipe(models.Model):
    nombre_receta= models.CharField(max_length=100, unique=True)
    ingredientes= models.TextField(help_text='Escribe los ingredientes')
    preparacion= models.TextField(verbose_name='Preparacion')
    tiempo_preparacion= models.IntegerField
    puntuacion= models.IntegerField
    fecha_publicacion= models.DateTimeField(auto_now=True)
    #usuario= models.ForeignKey(User)


