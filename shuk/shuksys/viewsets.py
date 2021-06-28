from django.shortcuts import render
from rest_framework import request, serializers, viewsets, mixins,permissions, authentication,views
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Lote, Producto, ProductoCategoria, Pedido, PedidoDetalle
from .serializers import LoteSerializer, ProductoSerializer, ProductoCategoriaSerializer, PedidoSerializer, PedidoDetalleSerializer
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
    serializer_class = PedidoSerializer
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
           return Pedido.objects.all()
        return Pedido.objects.filter(idUsuario = user.id)

class PedidoDetalleViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoDetalleSerializer
    queryset = PedidoDetalle.objects.all()

class LoteViewSet(viewsets.ModelViewSet):
    serializer_class = LoteSerializer
    queryset = Lote.objects.all()

