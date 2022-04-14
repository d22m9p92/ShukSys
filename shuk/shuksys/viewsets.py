from django.shortcuts import render
from rest_framework import request, serializers, viewsets, mixins,permissions, authentication,views, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Lote, Producto, ProductoCategoria, Pedido, PedidoDetalle
from .serializers import LoteSerializer, PedidoListaSerializer, ProductoSerializer, ProductoCategoriaSerializer, PedidoSerializer, PedidoDetalleSerializer
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
    
    def get_serializer_class(self):
        
        if self.action == 'list':
            return PedidoListaSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
           return Pedido.objects.all()
        return Pedido.objects.filter(idUsuario = user.id)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            import copy

            val_pedido = serializer.validated_data.copy()
            val_detalle = val_pedido.pop('detalle')

            #Guardar Pedido
            nuevo_pedido = Pedido(**val_pedido)
            nuevo_pedido.idUsuario = user
            nuevo_pedido.save()
    

            #Guardar Detalle
            for detalle_datos in val_detalle:
                detalle_nuevo = PedidoDetalle.objects.create(
                    idPedido = nuevo_pedido, **detalle_datos
                )
    
            return Response({'status':'ok','id':nuevo_pedido.pk},status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status=status.HTTP_400_BAD_REQUEST)   

class PedidoDetalleViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoDetalleSerializer
    permissions_classes = [IsAuthenticated]

    def get_queryset(self,pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return super().get_queryset()

    def list(self,request):
        print(request.data)
        detalle_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(request.data, status=status.HTTP_200_OK)


class LoteViewSet(viewsets.ModelViewSet):
    serializer_class = LoteSerializer
    queryset = Lote.objects.all()