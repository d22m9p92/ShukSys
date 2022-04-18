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

class PedidoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoDetalle
        fields = ['id','idProducto','cantidad']


class PedidoDetalleGetSerializer(serializers.ModelSerializer):
    idProducto = ProductoSerializer(many=False)
    
    class Meta:
        model = PedidoDetalle
        fields = ['id','idProducto','cantidad']


class PedidoSerializer(serializers.ModelSerializer):
    detalle = PedidoDetalleSerializer(many =True)

    class Meta:
        MethodNotAllowed
        model = Pedido
        fields = ['id','fechaPedido', 'numeroSeguimiento','idPedidoEstado','fechaDespacho','detalle','comentario','idLote']


class PedidoGetSerializer(serializers.ModelSerializer):
    idPedidoEstado = PedidoEstadoSerializer(many = False)
    detalle = PedidoDetalleGetSerializer(many =True)  

    class Meta:
        MethodNotAllowed
        model = Pedido
        fields = ['id','fechaPedido', 'numeroSeguimiento','idPedidoEstado','fechaDespacho','detalle','comentario','idLote']


class PedidoListaSerializer(serializers.ModelSerializer):
    idPedidoEstado = PedidoEstadoSerializer(many = False)

    class Meta:
        MethodNotAllowed
        model = Pedido
        fields = ['id','fechaPedido','idDetalleVenta', 'numeroSeguimiento','idPedidoEstado']
