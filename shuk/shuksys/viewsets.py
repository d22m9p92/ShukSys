from django.shortcuts import render
from rest_framework import serializers, viewsets, mixins,permissions, authentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Producto, ProductoCategoria, Pedido, PedidoDetalle
from .serializers import ProductoSerializer, ProductoCategoriaSerializer, PedidoSerializer, PedidoDetalleSerializer
from django.contrib.auth.models import User


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset =  Producto.objects.all()
  
class ProductoCategoriaViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,Token):
    permissions_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication] 
    serializer_class = ProductoCategoriaSerializer 
    queryset = ProductoCategoria.objects.all()
    
class PedidoViewSet(viewsets.ModelViewSet):
    permissions_classes = [AllowAny]
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

class PedidoDetalleViewSet(viewsets.ModelViewSet):
    #permissions_classes = [AllowAny]
    serializer_class = PedidoDetalleSerializer
    queryset = PedidoDetalle.objects.all()

