from rest_framework import serializers 
from . models import Clientes,Cuentas

class ClienteS (serializers.ModelSerializer):
    class Meta: 
        model = Clientes
        fields = ("id","nombre","apellidoPaterno",
                 "apellidoMaterno","correo")
        #depth = 1
class CuentaS (serializers.ModelSerializer):
    #cliente=ClienteS(many=True,read_only=True)
    class Meta:
        model=Cuentas
        fields = ("id","numero_tarjeta","saldo")
        #depth = 1