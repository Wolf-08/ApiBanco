from django.shortcuts import render
from django.http import JsonResponse
from .models import Clientes
from .models import Cuentas
from rest_framework import viewsets
from .serializers import ClienteS,CuentaS
# Create your views here.


# def index(request):
#     cuenta = Cuenta.objects.create(
#         numero_tarjeta = 1234567890987,
#         saldo=0,
#         #apellidoMaterno ='Sandoval',
#     )
#     cuenta.save()

# def getClientes(request):
#     cliente=Clientes.objects.all()
#     #query_cliente = Clientes.objects.get(id=1)
#     #query_cliente_cuenta = Cuenta.objects.get(id=1)
#     info = list(cliente.values("id","nombre"))
#     return JsonResponse(info,safe=False)

# def getCuentas(request):
#     cuenta=Cuentas.objects.all()
#     info = list(cuenta.values("saldo","cuenta"))
#     return JsonResponse(info,safe=False)

class ClienteSview(viewsets.ModelViewSet):
    serializer_class = ClienteS
    queryset=Clientes.objects.all()

class CuentaSview(viewsets.ModelViewSet):
    serializer_class = CuentaS
    queryset=Cuentas.objects.all()