import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ElectionRoutingModule} from "./election-routing.module";
import { CreateElectionRoundPageComponent } from './create-election-page/create-election-round-page.component';


@NgModule({
    declarations: [CreateElectionRoundPageComponent],
    imports: [
        CommonModule,
        ElectionRoutingModule
    ]
})
export class ElectionModule {
}
