import {Component} from '@angular/core';

@Component({
  selector: 'app-top-nav-bar',
  templateUrl: './top-nav-bar.component.html',
  styleUrls: ['./top-nav-bar.component.scss']
})
export class TopNavBarComponent {

  public links =  [
    {name: 'Home', route: '/home'},
    {name: 'Anmelden', route: '/'},
    {name: 'Mitgliederliste', route: '/persons'},
    {name: 'Mitglied erstellen', route: '/person/create'},
    {name: 'Wahl erstellen', route: '/election/create'},
    {name: 'Wahl', route: '/election'},
  ];

  constructor() { }

}
