import { Injectable } from '@angular/core';
import {LoginI,LoginO} from '../../modelos/login.interface';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs'; 

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  url:string = "http://127.0.0.1:8000/"

  constructor(private http:HttpClient) { }

  login(form:LoginI):Observable<LoginO >{
    let direccion = this.url + "api/login"
    let body = new FormData();
    body.append('username', form.usuario);
    body.append('password', form.password);
  
    return this.http.post<LoginO>(direccion,body)
  }
}
