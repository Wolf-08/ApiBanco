from rest_framework import serializers 
from . models import Clientes,Cuentas

class ClienteS (serializers.ModelSerializer):
    class Meta: 
        model = Clientes
        fields = ("id","nombre","apellidoPaterno",
                 "apellidoMaterno","correo")

class CuentaS (serializers.ModelSerializer):
    class Meta:
        model=Cuentas
        fields = ("id","numero_tarjeta","saldo")