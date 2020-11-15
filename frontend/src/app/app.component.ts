import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  public links =  [
    {name: 'Home', route: '/home'},
    {name: 'Anmelden', route: '/'},
    {name: 'Mitgliederliste', route: '/persons'},
    {name: 'Mitglied erstellen', route: '/person/create'},
    {name: 'Wahl erstellen', route: '/election/create'},
    {name: 'Wahl', route: '/election'},
  ]
}
