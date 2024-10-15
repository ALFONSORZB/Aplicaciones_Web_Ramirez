from django.db import models

from django.db import models

class iPhone(models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    almacenamiento = models.IntegerField()
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.modelo}"

class AirPods(models.Model):
    nombre = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.version}"


class MacBook(models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    almacenamiento = models.IntegerField()
    ram = models.IntegerField()
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.modelo}"



# Create your models here.
