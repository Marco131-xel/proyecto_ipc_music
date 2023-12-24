from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nit = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    
    def __str__(self):
        return self.nombre
