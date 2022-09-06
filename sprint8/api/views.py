from http import client
import re
from traceback import print_tb
from xml.etree.ElementTree import tostring
from django.shortcuts import render
from api.models import *
from api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions


# Create your views here.
class DatosCliente (APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente)
        if cliente:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaldoCuenta(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
         cuenta = Cuenta.objects.filter(pk=pk).first()
         serializer = CuentasSerializer(cuenta)
         if cuenta:
             return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class MontoPrestamo(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
         prestamo = Prestamo.objects.filter(customer_id=pk).first()
         serializer = PrestamoSerializer(prestamo)
         if prestamo:
            return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class PrestamosSucursal(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request,pk):
         prestamo = Prestamo.objects.filter(pk=pk).first()
         serializer = PrestamoSerializer(prestamo)
         if prestamo:
            return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class TarjetasCredito(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request,pk): 
         """ tar = Tarjeta.objects.filter(cliente_cuenta=pk).first() """
         tar=Tarjeta.objects.all()
         print(tar)
         serializer = TarjetaSerializer(tar)
         if tar:
            return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class PedirPrestamo(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request, format=None):
        serializer = PrestamoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnularPrestamo(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def delete(self, request, pk):
        pres = Prestamo.objects.filter(customer_id=pk).first()
        if pres:
            serializer = PrestamoSerializer(pres)
            pres.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class ModificarDireccion(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request,pk):
         dire = Direcciones.objects.filter(clien=pk)
         print(dire[1])
         
         serializer = DireccionesSerializer(dire,many=True)
         print(len(serializer.data))
         num=len(serializer.data)-1
         
         if dire:
            return Response(serializer.data[num], status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
   
    #def put(self, request,pk):
    #    dire = Direcciones.objects.filter(clien=pk)
    #    serializer = DireccionesSerializer(dire, data=request.data)
     #   if serializer.is_valid():
      #      serializer.save()
     #       return Response(serializer.data)
      #  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        cliente = Direcciones.objects.filter(pk=pk).first()
        serializer = DireccionesSerializer(cliente, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sucursales(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request):
         sucursal = Sucursal.objects.all().order_by('branch_number')
         serializer = SucursalSerializer(sucursal, many=True)
         if sucursal:
            return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
     