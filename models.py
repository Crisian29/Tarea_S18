from django.db import models

# Create your models here.
from django.db import models

class MiModelo(models.Model):
    # Campos del modelo
    nombre = models.CharField(max_length=255)
    # ...

    def __str__(self):
        return self.nombre

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.cliente.nombre} - {self.fecha}"
    
from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

from django.db import models

class Area(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
