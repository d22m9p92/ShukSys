from dataclasses import fields
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey

class ProductoCategoria(models.Model):
    descripcion = CharField(max_length =255, null=True)

    def __str__(self):
        return self.descripcion


class Producto(models.Model):
    descripcion = models.CharField(max_length =255, null=True)
    idProductoCategoria = models.ForeignKey(ProductoCategoria,related_name = 'productos' ,on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, default=None)

    def __str__(self):
       return self.descripcion

class PedidoEstado(models.Model):
    descripcion = models.CharField(max_length =255, null=True)
    
    def __str__(self):
       return self.descripcion

class Lote(models.Model):
    fechaDesde = models.DateField(auto_now=False, null=True)
    fechaHasta = models.DateField(auto_now=False, null=True)
    cerrado = models.BooleanField(default=False)

    def __int__(self):
       return self.pk

class Pedido(models.Model):
    idUsuario = models.ForeignKey(User,on_delete=models.CASCADE)
    fechaPedido = models.DateField(auto_now=True)
    horaPedido = models.TimeField(auto_now=True)
    numeroSeguimiento = models.CharField(max_length =255, null=True,blank=True)
    idPedidoEstado = models.ForeignKey(PedidoEstado,on_delete=models.CASCADE, related_name = 'estado')
    fechaDespacho = models.DateField(auto_now=False, null=True, default=None, blank=True)
    idDetalleVenta = models.IntegerField(null=True,blank=True)
    comentario = models.CharField(max_length =255, null=True,blank=True)
    idLote = models.ForeignKey(Lote, on_delete=models.CASCADE )
    #archivoDetalleVenta =

    def __int__(self):
       return self.pk

class PedidoDetalle(models.Model):
    idPedido = models.ForeignKey(Pedido,related_name = 'detalle',on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __int__(self):
       return self.pk

class Banco(models.Model):
    descripcion = models.CharField(max_length =255, null=True)

    def __str__(self):
       return self.descripcion

class CuentaBancaria(models.Model):
    cbu = models.BigIntegerField()
    numeroEntidad =  models.IntegerField()
    numeroSucursal = models.IntegerField()
    numerocuenta = models.BigIntegerField()
    idBanco = models.ForeignKey(Banco,on_delete=models.CASCADE)
