from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    anio_nacimiento = models.DateField()
