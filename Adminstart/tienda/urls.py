from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("carrito/", carrito, name="carrito"),
    path("user/", user, name="user"),
    path("producto/<int:producto_id>/", producto, name="producto"),
    path("ingresar/", ingresar, name="ingresar"),
    path("registrar/", registrar, name="registrar"),
    path("cerrar_sesion/", cerrar_sesion, name="cerrar"),
]
