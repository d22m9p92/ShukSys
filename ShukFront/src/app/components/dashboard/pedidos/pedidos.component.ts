import { Component, OnInit } from '@angular/core';

export interface PeriodicElement {
  name: string;
  imagen: string;
  cantidad: string;
}

const ELEMENT_DATA: PeriodicElement[] = [
  {imagen: 'imagen', name: 'Nombre de pan', cantidad: 'x'},
  {imagen: 'imagen 2', name: 'Nombre de pan 2', cantidad: 'x 2'},
  
];

@Component({
  selector: 'app-pedidos',
  templateUrl: './pedidos.component.html',
  styleUrls: ['./pedidos.component.css']
})
export class PedidosComponent implements OnInit {
  displayedColumns: string[] = ['imagen', 'name', 'cantidad'];
  dataSource = ELEMENT_DATA;
  constructor() { }

  ngOnInit(): void {
    this.firstFormGroup = this._formBuilder.group({
      firstCtrl: ['', Validators.required],
    });
    this.secondFormGroup = this._formBuilder.group({
      secondCtrl: ['', Validators.required],
    });
  }
}