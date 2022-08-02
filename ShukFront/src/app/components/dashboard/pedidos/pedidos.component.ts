import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/servicios/api/api.service';
import { Router } from '@angular/router';
import { ProductoCategoriaO } from 'src/app/modelos/pedidos.interface';

@Component({
  selector: 'app-pedidos',
  templateUrl: './pedidos.component.html',
  styleUrls: ['./pedidos.component.css']
})

export class PedidosComponent implements OnInit {
  displayedColumns: string[] = ['producto', 'cantidad'];
  dataProductos !: ProductoCategoriaO[];
  
  constructor(private api:ApiService, private router:Router) { }

  ngOnInit(): void {
    this.api.getProductoCategoria().subscribe(data =>{ 
      this.dataProductos = data;
      }
      ) 
  }
}