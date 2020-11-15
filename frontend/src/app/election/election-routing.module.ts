import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CreateElectionRoundPageComponent} from "./create-election-page/create-election-round-page.component";

const electionRoutes: Routes = [
  {path: 'election/create', component: CreateElectionRoundPageComponent }
];

@NgModule({
  imports: [
    RouterModule.forChild(electionRoutes)
  ],
  exports: [
    RouterModule
  ]
})
export class ElectionRoutingModule { }
