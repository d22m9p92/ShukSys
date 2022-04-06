import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Menu } from '../modelos/menu.interface';

@Injectable({
  providedIn: 'root'
})
export class MenuService {

  constructor(private http: HttpClient) { }

  /*################MENU############*/
  getMenu(): Observable<Menu[]>{
    return this.http.get<Menu[]>('./assets/data/menu.json');
  }
}
