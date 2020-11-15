import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LandingPageComponent } from './landing-page/landing-page.component';
import {LandingRoutingModule} from './landing-page-routing.module';



@NgModule({
  declarations: [LandingPageComponent],
  imports: [
    LandingRoutingModule,
    CommonModule
  ]
})
export class LandingPageModule { }
