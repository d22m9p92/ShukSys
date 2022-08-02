import { Injectable } from '@angular/core';
import {LoginI,LoginO} from '../../modelos/login.interface';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs'; 
import {PedidosO, ProductoCategoriaO} from '../../modelos/pedidos.interface';
import { tokenize } from '@angular/compiler/src/ml_parser/lexer';
import { Detalle } from 'src/app/modelos/detalle.interface';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  
  constructor(private http:HttpClient) { }


    /*################LOGIN############*/
  login(form:LoginI):Observable<LoginO >{
   
    let body = new FormData();
    body.append('username', form.usuario);
    body.append('password', form.password);
  
    return this.http.post<LoginO>('/api/login',body)
  }


    /*################PEDIDOS############*/
  getPedidos():Observable<PedidosO[]>{
    const headers = new HttpHeaders({'Authorization':'Token ' + localStorage.getItem('token')});
    return this.http.get<PedidosO[]>('/api/pedido/',  { headers: headers});
  }


  getDetalle(id):Observable<Detalle[]>{
    const headers = new HttpHeaders({'Authorization':'Token ' + localStorage.getItem('token')});
    return this.http.get<Detalle[]>('/api/pedidodetalle/'+id,  { headers: headers});
  }
<<<<<<< HEAD

  getProductoCategoria():Observable<ProductoCategoriaO[]>{
    const headers = new HttpHeaders({'Authorization':'Token ' + localStorage.getItem("token")});
    return this.http.get<ProductoCategoriaO[]>('/api/productocategoria',  { headers: headers});
  }

=======
>>>>>>> f83e4b25b11a26526f0b11c76593ea5e0b5afe5f
}
