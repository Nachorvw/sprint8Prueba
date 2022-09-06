from http import client
from django.contrib import admin
#from .models import User,Cliente,Sucursal,Empleado,Direccion,Tiposclientes,Prestamo,TipoCuenta,Cuenta,MarcaTarjeta,Tarjeta
from .models import *
# Register your models here.


class DatosAdmin(admin.ModelAdmin):
   
    #admin.site.register(User)
    admin.site.register(Cliente)
    admin.site.register(Sucursal)
    admin.site.register(Empleado)
    admin.site.register(Direcciones)
   # admin.site.register(Tiposclientes)
    admin.site.register(Prestamo)
   # admin.site.register(TipoCuenta)
    admin.site.register(Cuenta)
   # admin.site.register(MarcaTarjeta)
    admin.site.register(Tarjeta) 