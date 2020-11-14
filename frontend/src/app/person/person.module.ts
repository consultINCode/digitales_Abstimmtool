import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {PersonRoutingModule} from "./person-routing.module";
import { PersonOverviewPageComponent } from './person-overview-page/person-overview-page.component';
import { CreatePersonPageComponent } from './create-person-page/create-person-page.component';
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatInputModule} from "@angular/material/input";
import {ReactiveFormsModule} from "@angular/forms";

@NgModule({
  declarations: [
    PersonOverviewPageComponent,
    CreatePersonPageComponent
  ],
  exports: [
    PersonOverviewPageComponent
  ],
  imports: [
    CommonModule,
    PersonRoutingModule,
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule
  ]
})
export class PersonModule { }
