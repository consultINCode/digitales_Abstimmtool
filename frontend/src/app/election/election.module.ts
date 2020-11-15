import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ElectionRoutingModule} from "./election-routing.module";
import { CreateElectionRoundPageComponent } from './create-election-round-page/create-election-round-page.component';
import {MatCardModule} from "@angular/material/card";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatInputModule} from "@angular/material/input";
import {ReactiveFormsModule} from "@angular/forms";
import {MatButtonModule} from "@angular/material/button";
import {MatSelectModule} from "@angular/material/select";


@NgModule({
    declarations: [CreateElectionRoundPageComponent],
    imports: [
        CommonModule,
        ElectionRoutingModule,
        MatCardModule,
        MatFormFieldModule,
        MatInputModule,
        ReactiveFormsModule,
        MatButtonModule,
        MatSelectModule
    ]
})
export class ElectionModule {
}
