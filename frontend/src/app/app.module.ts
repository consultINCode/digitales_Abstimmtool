import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {environment} from '../environments/environment';
// App component
import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
// own modules
import {PersonModule} from './person/person.module';
import {LandingPageModule} from './landing-page/landing-page.module';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {ElectionModule} from './election/election.module';
import {TopNavBarComponent} from "./core/components/top-nav-bar/top-nav-bar.component";
import {MatToolbarModule} from '@angular/material/toolbar';


@NgModule({
  declarations: [
    AppComponent,
    TopNavBarComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    // own Modules
    PersonModule,
    LandingPageModule,
    ElectionModule
  ],
  providers: [
    {provide: 'DEM_API_URL', useValue: environment.demApiUrl},
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
