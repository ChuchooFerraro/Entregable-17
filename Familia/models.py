from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    age = models.IntegerField()
    born = models.DateField()
    rango = models.CharField(max_length=40)


