import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard.component';
import { PedidosComponent } from './pedidos/pedidos.component';
import { MispedidosComponent } from './mispedidos/mispedidos.component';

const routes: Routes = [
  {path: '', component: DashboardComponent, children: [
    { path: '',component: MispedidosComponent, },
    { path: 'nuevopedido',component: PedidosComponent, }
  ]}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardRoutingModule { }
