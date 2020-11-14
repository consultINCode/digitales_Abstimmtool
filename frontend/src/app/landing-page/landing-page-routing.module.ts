import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {LandingPageComponent} from "./landing-page/landing-page.component";

const landingRoutes: Routes = [
    { path: 'home', component: LandingPageComponent},
];

@NgModule({
    imports: [
        RouterModule.forChild(landingRoutes)
    ],
    exports: [
        RouterModule
    ]
})

export class LandingRoutingModule {

}
