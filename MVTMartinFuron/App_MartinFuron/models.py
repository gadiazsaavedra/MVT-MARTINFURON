from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class   familia(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    email = models.EmailField()
    mayor_de_edad = models.BooleanField()
    cumpleaños= models.DateField()




