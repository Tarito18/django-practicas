from django.db import models

# Create your models here.
class curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()

class profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()  
    profesion = models.CharField(max_length=30)

class entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
