"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from banco import views

router = routers.DefaultRouter()
router.register(r'clientes',views.ClienteSview,'banco')
router.register(r'cuentas',views.CuentaSview,'banco')
router.register(r'cuentaCliente',views.CuentaClienteView,'banco')
#router.register(r'clientesV',views.OnlyVIsta,'banco')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include(router.urls)),
    path("clientesV/",views.OnlyVIstaClientes.as_view()),
    path("cuentasV/",views.OnlyVIstaCuentas.as_view())
    #path("cuentas",include("banco.urls")),
]
