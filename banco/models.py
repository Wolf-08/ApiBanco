from django.db import models
import uuid

# Create your models here.
class Clientes (models.Model):
    nombre=models.TextField(null=False)
    apellidoPaterno= models.TextField(null=False)
    apellidoMaterno= models.TextField(null=True)
    correo=models.TextField(null=True)
    def __str__(self):
        return self.nombre
    
class Cuentas(models.Model):
    numero_tarjeta=models.PositiveIntegerField(default=0)
    saldo=models.PositiveIntegerField(default=0)
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

# class Movimiento (models.Model):
#     tipo_transaccion=models.TextField(null=False)
#     monto=models.SmallIntegerField()
#     cuenta=models.OneToOneField(Cuenta,on_delete=models.SET_NULL,null=True)
