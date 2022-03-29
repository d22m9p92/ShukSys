from pyexpat import model
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed
from .models import Lote, PedidoEstado, Producto, ProductoCategoria , Pedido, PedidoDetalle

'''############LISTADO DE PRODUCTOS############'''
class PedidoEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoEstado
        fields =  ['id','descripcion']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','descripcion','imagen']

class ProductoCategoriaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True) 
    
    class Meta:
        MethodNotAllowed
        model = ProductoCategoria
        fields = ['id','descripcion','productos']


'''############PEDIDOS############'''
class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    idPedidoEstado = PedidoEstadoSerializer(many = False)

    class Meta:
    
        model = Pedido
        fields = ['id','idUsuario','fechaPedido', 'numeroSeguimiento','idPedidoEstado','fechaDespacho','idDetalleVenta','comentario','idLote']

class PedidoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoDetalle
        fields = '__all__'
