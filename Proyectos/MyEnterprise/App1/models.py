from typing_extensions import runtime
from django.db import models

# Create your models here.
class Cliente(models.Model):
    # se está creando un id automáticamente
    nombre = models.CharField(max_length=50)
    run = models.IntegerField()
    dv = models.IntegerField()

class Cuentas(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    n_cuenta = models.IntegerField()
    saldo = models.FloatField()