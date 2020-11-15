import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {PersonOverviewPageComponent} from './person-overview-page/person-overview-page.component';
import {CreatePersonPageComponent} from './create-person-page/create-person-page.component';

const personRoutes: Routes = [
  { path: 'persons', component: PersonOverviewPageComponent},
  { path: 'person/create', component: CreatePersonPageComponent},
];

@NgModule({
  imports: [
    RouterModule.forChild(personRoutes)
  ],
  exports: [
    RouterModule
  ]
})

export class PersonRoutingModule {

}
