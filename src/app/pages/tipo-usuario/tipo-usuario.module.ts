import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { TipoUsuarioPageRoutingModule } from './tipo-usuario-routing.module';

import { TipoUsuarioPage } from './tipo-usuario.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    TipoUsuarioPageRoutingModule,
    ReactiveFormsModule
  ],
  declarations: [TipoUsuarioPage]
})
export class TipoUsuarioPageModule {}
