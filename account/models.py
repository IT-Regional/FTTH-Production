from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


class Cliente(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre del cliente")
    apellido = models.CharField(max_length=250, verbose_name="Apellidos del cliente")
    email = models.EmailField(max_length=250, verbose_name="Correo del Cliente")
    addres = models.CharField(max_length=250, verbose_name="Direccion del Cliente")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.nombre