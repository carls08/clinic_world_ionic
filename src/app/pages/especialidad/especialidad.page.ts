import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-especialidad',
  templateUrl: './especialidad.page.html',
  styleUrls: ['./especialidad.page.scss'],
})
export class EspecialidadPage implements OnInit {
formEspecialidad : FormGroup
  constructor(
    public fb:FormBuilder
  ) {
    this.formEspecialidad = this.fb.group({
      'nombre' : ['',[Validators.required]],
      'descripcion' : ['',[Validators.required]]
    })
   }

  ngOnInit() {
  }

}
