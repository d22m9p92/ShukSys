import { Component, OnInit} from '@angular/core';

export interface Pedidos {
  nropedido: number;
  estado: string;
  fechadespacho: string;
  observacion: string;
  nroseguimiento: number;
  detalle: string;
}

const ListaPedidos: Pedidos[] = [
  {nropedido: 1, estado: 'en camino', fechadespacho: '18/2/2022', observacion: 'nada', nroseguimiento: 12,detalle: 'nada'},
];

@Component({
  selector: 'app-mispedidos',
  templateUrl: './mispedidos.component.html',
  styleUrls: ['./mispedidos.component.css']
})
export class MispedidosComponent implements OnInit {

  displayedColumns: string[] = ['nropedido', 'estado', 'fechadespacho',  'observacion', 'nroseguimiento', 'detalle'];
  dataSource = ListaPedidos;
  clickedRows = new Set<Pedidos>();

  constructor() { }

  ngOnInit(): void {
  }

}
