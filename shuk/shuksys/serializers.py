from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed
from .models import Producto, ProductoCategoria  

'''############LISTADO DE PRODUCTOS############'''
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','descripcion']

class ProductoCategoriaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True) 
    
    class Meta:
        MethodNotAllowed
        model = ProductoCategoria
        fields = ['id','descripcion','productos']