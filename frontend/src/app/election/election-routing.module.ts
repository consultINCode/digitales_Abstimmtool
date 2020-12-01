import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CreateElectionRoundPageComponent} from './create-election-round-page/create-election-round-page.component';
import {ElectionOverviewPageComponent} from './election-overview-page/election-overview-page.component';

const electionRoutes: Routes = [
  {path: 'election/create', component: CreateElectionRoundPageComponent },
  {path: 'election', component: ElectionOverviewPageComponent},
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
