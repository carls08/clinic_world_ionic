import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-tipo-usuario',
  templateUrl: './tipo-usuario.page.html',
  styleUrls: ['./tipo-usuario.page.scss'],
})
export class TipoUsuarioPage implements OnInit {
formTipo_usuario : FormGroup
  constructor(
    public fb :FormBuilder
  ) {
    this.formTipo_usuario = this.fb.group({
      'nombre': ['', [Validators.required]],
      'descripcion': ['', [Validators.required]]
    });
   }

  ngOnInit() {
  }

}
