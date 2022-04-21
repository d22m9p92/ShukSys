import { Component, OnInit, ViewChild } from '@angular/core';
import { PedidosO } from 'src/app/modelos/pedidos.interface';
import { MatPaginator } from '@angular/material/paginator';
import { ApiService } from 'src/app/servicios/api/api.service';
import { Router } from '@angular/router';
import { MatTableDataSource } from '@angular/material/table';


@Component({
  selector: 'app-pedidodetalle',
  templateUrl: './pedidodetalle.component.html',
  styleUrls: ['./pedidodetalle.component.css']
})
export class PedidodetalleComponent implements OnInit {
  displayedColumns: string[] = ['idProducto', 'cantidad'];
  dataDetalle: any;
  
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  constructor(private api:ApiService, private router:Router) { }

  ngOnInit(): void {
    this.api.getPedidos().subscribe(data =>{ 
      this.dataDetalle = new MatTableDataSource(data);
      this.dataDetalle.paginator = this.paginator;
      }
      )
  }
}
