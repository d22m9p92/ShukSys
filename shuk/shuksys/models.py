from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey

'''
class User(AbstractUser):
    idContagram = models.IntegerField()

    class Meta:
        db_table = 'auth_user'
'''

class ProductoCategoria(models.Model):
    descripcion = CharField(max_length =255, null=True)

    def __str__(self):
        return self.descripcion


class Producto(models.Model):
    descripcion = models.CharField(max_length =255, null=True)
    idProductoCategoria = models.ForeignKey(ProductoCategoria,related_name = 'productos' ,on_delete=models.CASCADE)

    def __str__(self):
       return self.descripcion

class PedidoEstado(models.Model):
    descripcion = models.CharField(max_length =255, null=True)
    
    def __str__(self):
       return self.descripcion

class Pedido(models.Model):
    idUsuario = models.ForeignKey(User,on_delete=models.CASCADE)
    fechaPedido = models.DateTimeField(auto_now=True)
    numeroSeguimiento = models.CharField(max_length =255, null=True)
    idPedidoEstado = models.ForeignKey(PedidoEstado,on_delete=models.CASCADE)
    fechaDespacho = models.DateTimeField(auto_now=False, null=True, default=None)
    idDetalleVenta = models.IntegerField(null=True)
    comentario = models.CharField(max_length =255, null=True)
    #archivoDetalleVenta =
    
    def __int__(self):
       return self.pk

class PedidoDetalle(models.Model):
    idPedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()

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


