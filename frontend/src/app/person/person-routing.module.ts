import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {PersonOverviewPageComponent} from "./person-overview-page/person-overview-page.component";

const personRoutes: Routes = [
  { path: 'person', component: PersonOverviewPageComponent},
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
