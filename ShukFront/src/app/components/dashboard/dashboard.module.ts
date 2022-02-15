import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardRoutingModule } from './dashboard-routing.module';
import { SharedModule } from '../shared/shared.module';
import { DashboardComponent } from './dashboard.component';
import { PedidosComponent } from './pedidos/pedidos.component';
import { NavbarComponent } from './navbar/navbar.component';
import { MispedidosComponent } from './mispedidos/mispedidos.component';


@NgModule({
  declarations: [
    DashboardComponent,
    NavbarComponent,
    PedidosComponent,
    MispedidosComponent
  ],
  imports: [
    CommonModule,
    DashboardRoutingModule,
    SharedModule
  ]
})
export class DashboardModule { }
