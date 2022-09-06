from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TCuenta(models.Model):
    cuenta_id = models.AutoField(primary_key=True,null=False, blank=True)
    descipcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'T_cuenta'


class Tclien(models.Model):
    customer_id = models.AutoField(primary_key=True, blank=True, null=False)
    type_des = models.TextField()

    class Meta:
        managed =False
        db_table = 'Tclien'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direcciones(models.Model):
    calle = models.TextField()
    numero = models.IntegerField(primary_key=True)
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    emple = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='emple')
    clien = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='clien')
    sucur = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='sucur')

    class Meta:
        managed = False
        db_table = 'direcciones'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class MTarjetas(models.Model):
    credit_id = models.AutoField(primary_key=True, blank=True, null=False)
    nombre_credito = models.TextField()

    class Meta:
        managed = False
        db_table = 'm_tarjetas'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    id = models.CharField(max_length=200,db_column='id' ,primary_key=True)
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    fecha_otorgamiento = models.TextField(db_column='Fecha_Otorgamiento', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecha_expiracion = models.TextField(db_column='fecha_Expiracion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tipo_tarjeta = models.TextField()
    marca = models.ForeignKey(MTarjetas, models.DO_NOTHING, db_column='marca')
    cliente_cuenta = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='Cliente_cuenta')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tarjeta'