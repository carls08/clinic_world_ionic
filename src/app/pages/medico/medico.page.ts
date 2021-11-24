import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-medico',
  templateUrl: './medico.page.html',
  styleUrls: ['./medico.page.scss'],
})
export class MedicoPage implements OnInit {
formMedico:FormGroup;
  constructor(
    public fb: FormBuilder
  ) {
    this.formMedico = this.fb.group({
      'idUsuario' : ['',[Validators.required]],
      'idEspecialidad' :  ['',[Validators.required]],
      'fecha_creacion' :  ['',[Validators.required]]
    })

   }

  ngOnInit() {
  }

}
