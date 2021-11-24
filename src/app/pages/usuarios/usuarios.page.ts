import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-usuarios',
  templateUrl: './usuarios.page.html',
  styleUrls: ['./usuarios.page.scss'],
})
export class UsuariosPage implements OnInit {
formUsuarios : FormGroup

  constructor(
    public fb: FormBuilder
  ) { this.formUsuarios = this.fb.group({
    'tipo_documento': ['', [Validators.required]],
    'numero_documento': ['', [Validators.required]],
    'edad':['',[Validators.required]],
    'nombre' : ['',[Validators.required]],
    'segundo_nombre': ['', [Validators.required]],
    'apellido': ['', [Validators.required]],
    'segundo_apellido' : ['',[Validators.required]],
    'direccion': ['', [Validators.required]],
    'telefono': ['', [Validators.required]],
    'idTipo_usuario' : ['',[Validators.required]],
    'correo': ['', [Validators.required]],
    'usuario': ['', [Validators.required]],
    'contraseña' : ['',[Validators.required]]
  });
    
  }

  ngOnInit() {
  }

}
