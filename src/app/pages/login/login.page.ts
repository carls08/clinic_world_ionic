import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  formLogin: FormGroup;

  constructor(
    public fb: FormBuilder
  ) { 
    this.formLogin = this.fb.group({
      'usuario': ['', [Validators.required]],
      'contraseña': ['', [Validators.required]]
    });
  }

  ngOnInit() {
  }

  Ingresar() {
    alert('Hi');
  }
}
