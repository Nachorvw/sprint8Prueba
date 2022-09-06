from dataclasses import field
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class PrestamoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Prestamo
        fields = "__all__"


class CuentasSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Cuenta
        fields = "__all__"


class SucursalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Sucursal
        fields = "__all__"
        


class DireccionesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Direcciones
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Cliente
        fields = "__all__"


class TarjetaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Tarjeta
        fields = "__all__"