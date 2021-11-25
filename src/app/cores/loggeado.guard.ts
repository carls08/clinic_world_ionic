import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, UrlTree } from '@angular/router';
import { NavController } from '@ionic/angular';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoggeadoGuard implements CanActivate {

  constructor(
    public navController: NavController
  ) { }

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    //verificacion loggin
    const auth = localStorage.getItem('dataUser');
    if (auth) {
      return true;
    }
    this.navController.navigateRoot('loggin');
    return false;
  }

}
