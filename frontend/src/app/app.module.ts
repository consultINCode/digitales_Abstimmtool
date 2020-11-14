import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from "@angular/common/http";
import {environment} from "../environments/environment";
// App component
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
// own modules
import {PersonModule} from "./person/person.module";
import {LandingPageModule} from "./landing-page/landing-page.module";


@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    PersonModule,
    LandingPageModule
  ],
  providers: [
    {provide: 'DEM_API_URL', useValue: environment.demApiUrl},
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
