import { Component, OnInit, ViewChild } from '@angular/core';
import { Detalle } from 'src/app/modelos/detalle.interface';
import { MatPaginator } from '@angular/material/paginator';
import { ApiService } from 'src/app/servicios/api/api.service';
import { Router, ActivatedRoute } from '@angular/router';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-pedidodetalle',
  templateUrl: './pedidodetalle.component.html',
  styleUrls: ['./pedidodetalle.component.css']
})

export class PedidodetalleComponent implements OnInit {

  displayedColumns: string[] = ['idProducto','cantidad'];
  dataDetalle: any;

  @ViewChild(MatPaginator) paginator!: MatPaginator;

  constructor(private api:ApiService, private acttiverouter:ActivatedRoute,private router:Router) { }

  ngOnInit(): void {
    let detalleid = this.acttiverouter.snapshot.paramMap.get('id');
    let token = this.getToken();
    this.api.getDetalle(detalleid).subscribe(data =>{
      this.dataDetalle = new MatTableDataSource(data);
      console.log(this.dataDetalle)
      //this.dataDetalle.paginator = this.paginator;
      }
      )
  }

  getToken(){
    return localStorage.getItem('token')
  }
}
