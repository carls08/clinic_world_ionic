import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { LoggeadoGuard } from './cores/loggeado.guard';
import { NoLoggeadoGuard } from './cores/no-loggeado.guard';
import { LayoutComponent } from './pages/layout/layout.component';

const routes: Routes = [
  {
    path: 'main',
    component: LayoutComponent,
    canActivate: [LoggeadoGuard]
  },
  {
    path: 'loggin',
    loadChildren: () => import('./pages/login/login.module').then(m => m.LoginPageModule),
    // canActivate: [NoLoggeadoGuard]
  },
  {
    path: 'medico',
    loadChildren: () => import('./pages/medico/medico.module').then(m => m.MedicoPageModule),
    canActivate: [LoggeadoGuard]
  },
  {
    path: 'citas',
    loadChildren: () => import('./pages/citas/citas.module').then(m => m.CitasPageModule),
    canActivate: [LoggeadoGuard]
  },
  {
    path: 'clientes',
    loadChildren: () => import('./pages/clientes/clientes.module').then(m => m.ClientesPageModule),
    canActivate: [LoggeadoGuard]
  },
  {
    path: 'usuarios',
    loadChildren: () => import('./pages/usuarios/usuarios.module').then(m => m.UsuariosPageModule),
    canActivate: [LoggeadoGuard]
  },
  {
    path: 'tipo-usuario',
    loadChildren: () => import('./pages/tipo-usuario/tipo-usuario.module').then(m => m.TipoUsuarioPageModule),
    canActivate: [LoggeadoGuard]
  },
  {
    path: '',
    redirectTo: '/loggin',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
