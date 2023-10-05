from django.db import models
 
class Flota(models.Model):
    marcaModelo = models.CharField(max_length=30)
    anio = models.IntegerField()
    km = models.IntegerField()
    transmision = models.CharField(max_length=30)
    combustible = models.CharField(max_length=30)
    costo = models.IntegerField()
    foto = models.CharField(max_length=100)
 
class Chofer(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    puesto = models.CharField(max_length=30)
    foto = models.CharField(max_length=100)

class PuntoDeRetiro(models.Model):
    provincia = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

    