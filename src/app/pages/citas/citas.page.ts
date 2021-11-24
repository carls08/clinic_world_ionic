import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-citas',
  templateUrl: './citas.page.html',
  styleUrls: ['./citas.page.scss'],
})
export class CitasPage implements OnInit {
formCitas : FormGroup;
  constructor(
    public fb: FormBuilder
  ) { this.formCitas = this.fb.group({
    'idCliente': ['', [Validators.required]],
    'idEspecialidad_nedico': ['', [Validators.required]],
    'fecha_hora': ['',[Validators.required]]
  });

  }

  ngOnInit() {
  }

}
