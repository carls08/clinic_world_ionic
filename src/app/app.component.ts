import { Component } from '@angular/core';
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  public appPages = [
    { title: 'Inbox', url: '/folder/Inbox', icon: 'mail' },
    { title: 'Medico', url: 'medico', icon: 'paper-plane' },
    { title: 'Citas', url: 'citas', icon: 'paper-plane' },
    { title: 'Clientes', url: 'clientes', icon: 'paper-plane' },
   
  ];
  public labels = ['Family', 'Friends', 'Notes', 'Work', 'Travel', 'Reminders'];
  constructor() {}
}
