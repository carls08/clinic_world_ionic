import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TipoUsuarioService {

  url = "http://127.0.0.1:3000/";

  constructor(private http: HttpClient) { }


  //OBTENER TODOS LOS DATOS
  getAlltipo(){
    console.log(this.http.get(`${this.url}getAlltipo`))
    return this.http.get(`${this.url}getAlltipo`);
  }
  //insertar
  alta(tusuarios:any):Observable<any>{
    return this.http.post(`${this.url}addTipo`, tusuarios);
  }
}
