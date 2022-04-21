import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/servicios/api/api.service';
import { PedidosO } from '../../../modelos/pedidos.interface'
import {MatPaginator, PageEvent} from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-mispedidos',
  templateUrl: './mispedidos.component.html',
  styleUrls: ['./mispedidos.component.css']
})

export class MispedidosComponent implements OnInit {

  displayedColumns: string[] = ['fechaPedido','idPedidoEstado','idDetalleVenta','detalle'];
  dataPedido: any; //Es de tipo PedidosO[]
  
  
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  constructor(private api:ApiService, private router:Router) { }

  ngOnInit(): void {
    this.api.getPedidos().subscribe(data =>{ 
      this.dataPedido = new MatTableDataSource(data);
      this.dataPedido.paginator = this.paginator;
      }
      )
    
  }


}

