import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {PersonRoutingModule} from "./person-routing.module";
import { PersonOverviewPageComponent } from './person-overview-page/person-overview-page.component';

@NgModule({
  declarations: [
    PersonOverviewPageComponent
  ],
  exports: [
    PersonOverviewPageComponent
  ],
  imports: [
    CommonModule,
    PersonRoutingModule
  ]
})
export class PersonModule { }
