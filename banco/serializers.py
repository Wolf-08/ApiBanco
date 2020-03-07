from rest_framework import serializers 
from . models import Clientes,Cuentas,CuentaCliente

class ClienteS (serializers.ModelSerializer):
    class Meta: 
        model = Clientes
        fields = ("id","nombre","apellidoPaterno",
                 "apellidoMaterno","correo")
        #depth = 1
class CuentaS (serializers.ModelSerializer):
    client=serializers.CharField(source="cliente",read_only=True)
    class Meta:
        model=Cuentas
        fields = ("id","numero_tarjeta","saldo","client")
        #depth = 1
class CuentaClienteS(serializers.ModelSerializer):
    user=serializers.CharField(source="cliente_id",read_only=True)
    titular=serializers.CharField(source="cuenta_id",read_only=True)
    saldoT=CuentaS(source="saldo",read_only=True)
    class Meta:
        model=CuentaCliente
        fields=("id","titular","user","saldoT","fecha_consultaC")