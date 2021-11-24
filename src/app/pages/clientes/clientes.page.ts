import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-clientes',
  templateUrl: './clientes.page.html',
  styleUrls: ['./clientes.page.scss'],
})
export class ClientesPage implements OnInit {
formClientes : FormGroup
  constructor(
    public fb: FormBuilder
  ) { this.formClientes =  this.fb.group({
    'tipo_documento': ['',[Validators.required]],
    'numero_documento': ['',[Validators.required]],
    'edad': ['',[Validators.required]],
    'nombre': ['',[Validators.required]],
    'segundo_nombre': ['',[Validators.required]],
    'apellido': ['',[Validators.required]],
    'segundo_apellido': ['',[Validators.required]],
    'direccion': ['',[Validators.required]],
    'telefono': ['',[Validators.required]],
    'usuario': ['',[Validators.required]],
    'contraseña': ['',[Validators.required]]
  })
    
   }

  ngOnInit() {
  }

}
