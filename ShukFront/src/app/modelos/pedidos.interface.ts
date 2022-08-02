export interface PedidosO{
    id: Number;
    fechaPedido: Date;
    numeroSeguimiento: Number;
    fechaDespacho: Date;
    idDetalleVenta: Number;
    comentario: String; 
    idUsuario: Number;
    idPedidoEstado: any;
    idLote: Number;
    detalle: any
};


export interface ProductoCategoriaO{
    id: Number;
    descripcion: String;
    productos: any;
}