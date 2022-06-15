import { Component, OnInit, ViewChild,Input } from '@angular/core';
import { Detalle } from 'src/app/modelos/detalle.interface';
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
  dataDetalle: Detalle[]=[];
  
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  constructor(private api:ApiService, private router:Router) { }

  ngOnInit(): void {
    this.api.getDetalle().subscribe(data =>{ 
      this.dataDetalle = data;
      //this.dataDetalle.paginator = this.paginator;
      }
      )
  }
}
