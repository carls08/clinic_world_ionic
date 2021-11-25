import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { TipoUsuarioService } from 'src/app/services/tipo-usuario.service';
import { AlertController } from '@ionic/angular';
@Component({
  selector: 'app-tipo-usuario',
  templateUrl: './tipo-usuario.page.html',
  styleUrls: ['./tipo-usuario.page.scss'],
})
export class TipoUsuarioPage implements OnInit {
formTipo_usuario : FormGroup
  constructor( public alertController: AlertController,private fb :FormBuilder, private tusuarios : TipoUsuarioService) {
    this.formTipo_usuario = this.fb.group({
      'nombre': ['', [Validators.required]],
      'descripcion': ['', [Validators.required]]
    });
   }
   
  addTipo: any;
   nuevocon={
     nombre:null,
     descripcion:null
     
   }
 
   alta(value:any) {
    console.log(value);
    this.nuevocon={
      nombre:value.nombre,
      descripcion:value.descripcion
  
    }
    this.tusuarios.alta(this.nuevocon).subscribe(datos => {
      console.log(datos)
      this.formTipo_usuario.reset()
      this.showAlert()
     });
  }

  showAlert() {

    this.alertController.create({
      header: 'Informacion',
      subHeader: 'gestion de tipo de usuarios',
      message: ' tipo de usuario agregado',
      buttons: ['OK']
    }).then(res => {

      res.present();

    });

  }


  ngOnInit() {
  }

}
