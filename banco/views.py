from django.shortcuts import render
from django.http import JsonResponse
from .models import Clientes
from .models import Cuentas
from rest_framework import viewsets,generics
from .serializers import ClienteS,CuentaS
from . import serializers, models
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class ClienteSview(viewsets.ModelViewSet):
    serializer_class = ClienteS
    queryset=Clientes.objects.all()
    # @api_view(['GET','POST'])
    # def clientes(request):
    #     if request.method == 'POST':
    #         return Response({"Usuario":Clientes.objects.all()})

class CuentaSview(viewsets.ModelViewSet):
    serializer_class = CuentaS
    queryset=Cuentas.objects.all()

class OnlyVIstaClientes(generics.ListAPIView):
    serializer_class = ClienteS
    queryset=Clientes.objects.all()
    

class OnlyVIstaCuentas(generics.ListAPIView):
    serializer_class = CuentaS
    queryset=Cuentas.objects.all()
