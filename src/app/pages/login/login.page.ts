import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AlertController, NavController } from '@ionic/angular';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  formLogin: FormGroup;

  constructor(
    public fb: FormBuilder,
    public alertController: AlertController,
    public loginService: LoginService,
    public navController: NavController
  ) {
    this.formLogin = this.fb.group({
      'usuario': ['', [Validators.required]],
      'contraseña': ['', [Validators.required]]
    });
  }

  ngOnInit() {
  }

  Ingresar() {
    if (this.formLogin.invalid) {
      this.alerta('Informacion Incompleta', 'Por favor ingrese todos los campos');
      return;
    }
    //EXECUTION CODE
    const usuario = this.formLogin.value;
    //VAR TO VERIFY
    this.loginService.verificarUsuario(usuario).subscribe(res => {
      if(!res) {
       this.alerta('Datos Incorrectos', 'El usuario y/o contraseña ingresados son Incorrectos o Inexistentes');
       return;
      }
      // Agregamos la informacion al storage para verificar
      localStorage.setItem('dataUser', JSON.stringify(res));
      //redirigimos
      this.navController.navigateRoot('main');
    });
  }

  async alerta(titulo, texto) {
    const alert = await this.alertController.create({
      cssClass: 'my-custom-class',
      header: titulo,
      message: texto,
      buttons: ['Entendido']
    });

    await alert.present();
  }
}
