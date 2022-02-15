from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed
from .models import Lote, Producto, ProductoCategoria , Pedido, PedidoDetalle

'''############LISTADO DE PRODUCTOS############'''
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
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoDetalle
        fields = '__all__'
