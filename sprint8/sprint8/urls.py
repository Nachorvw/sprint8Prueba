"""sprint8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/datos/<int:pk>/',DatosCliente.as_view()),#get
    path('api/cuenta/<int:pk>/',SaldoCuenta.as_view()),#get
    path('api/prestamos/<int:pk>/',MontoPrestamo.as_view()),#get
    path('api/prestamossucursal/<int:pk>/',PrestamosSucursal.as_view()),#get
    path('api/tarcredito/<int:pk>/',TarjetasCredito.as_view()), #get
    path('api/pedir/',PedirPrestamo.as_view()),#post
    path('api/anular/<int:pk>/',AnularPrestamo.as_view()),#delate
    path('api/modificar/<int:pk>/',ModificarDireccion.as_view()), #put
    path('api/sucursales/',Sucursales.as_view()), #get 
    path('api-auth/', include('rest_framework.urls')),
]

