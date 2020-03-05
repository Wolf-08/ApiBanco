from django.db import models
from django.utils import timezone
import uuid
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
class Clientes (models.Model):
    nombre=models.TextField(null=False)
    apellidoPaterno= models.TextField(null=False)
    apellidoMaterno= models.TextField(null=True)
    correo=models.TextField(null=True)
    def __str__(self):
        return self.nombre
    
class Cuentas(models.Model):
    numero_tarjeta=models.CharField(max_length=15)
    saldo=models.PositiveIntegerField(default=0)
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    fecha_consulta= models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.id)
class CuentaCliente(models.Model):
    cuenta_id =    models.ForeignKey(Cuentas,on_delete=models.CASCADE)
    cliente_id =  models.ForeignKey(Clientes,on_delete=models.CASCADE)
    fecha_consultaC = models.DateTimeField(default=timezone.now)