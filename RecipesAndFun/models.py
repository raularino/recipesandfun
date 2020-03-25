from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class receta(models.Model):
    nombre_receta= models.CharField(max_length=100)
    ingredientes= models.TextField(help_text='Escribe los ingredientes')
    preparacion= models.TextField(verbose_name='Preparacion')
    tiempo_preparacion= models.IntegerField
    comentarios= models.CharField(help_text='Espacio para comentarios', max_length=1000, null=True)
    puntuacion= models.IntegerField
    fecha_publicacion= models.DateTimeField(blank=True, null=True)
    #autor= models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.nombre_receta

    def create(self):
        self.fecha_publicacion=timezone.now()

class ingrediente(models.Model):
    nombre_ingrediente=models.CharField(max_length=30)
    tipo=models.CharField(max_length=50)
