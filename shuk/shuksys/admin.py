from django.contrib import admin
from .models import Producto,ProductoCategoria,PedidoEstado,Pedido,PedidoDetalle,Banco,CuentaBancaria

admin.site.register(Producto)
admin.site.register(ProductoCategoria)
admin.site.register(PedidoEstado)
admin.site.register(Pedido)
admin.site.register(PedidoDetalle)
admin.site.register(Banco)
admin.site.register(CuentaBancaria)
