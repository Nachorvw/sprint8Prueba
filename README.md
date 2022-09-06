# Sprint-8
# Rutas API del Homebanking

# get  
**OBTENER DATOS DE UN CLIENTE : http://127.0.0.1:8000/api/datos/5/**  
**OBTENER SALDO DE CUENTA DE UN CLIENTE : http://127.0.0.1:8000/api/cuenta/5/**  
**OBTENER MONTO DE PRESTAMOS DE UN CLIENTE : http://127.0.0.1:8000/api/prestamos/254/**  
**OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL: http://127.0.0.1:8000/api/prestamossucursal/5/**  
**LISTADO DE TODAS LAS SUCURSALES: http://127.0.0.1:8000/api/sucursales/**  
**VER DIRECCIONES DE UN CLIENTE : http://127.0.0.1:8000/api/modificar/25/**
# post  
**GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE: http://127.0.0.1:8000/api/pedir/**  
  {
    "loan_type": "HIPOTECARIO",
    "loan_date": "2022-12-26",
    "loan_total": 42881522,
    "customer_id": 251
  }
# delete  
**ANULAR SOLICITUD DE PRESTAMO DE CLIENTE:  http://127.0.0.1:8000/api/anular/100/**  
# put  
**MODIFICAR DATOS DE UN CLIENTE : http://127.0.0.1:8000/api/datos/5/**  
**MODIFICAR DIRECCIONES DE UN CLIENTE : http://127.0.0.1:8000/api/modificar/25/**
