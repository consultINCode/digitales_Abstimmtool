import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ElectionRoutingModule} from './election-routing.module';
import { CreateElectionRoundPageComponent } from './create-election-round-page/create-election-round-page.component';
import {MatCardModule} from '@angular/material/card';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {ReactiveFormsModule} from '@angular/forms';
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import { ElectionOverviewPageComponent } from './election-overview-page/election-overview-page.component';
import {MatTableModule} from '@angular/material/table';
import { CreateChoicesComponent } from './create-choices/create-choices.component';
import { ListChoicesComponent } from './list-choices/list-choices.component';
import {MatIconModule} from '@angular/material/icon';


@NgModule({
    declarations: [
        CreateElectionRoundPageComponent,
        ElectionOverviewPageComponent,
        CreateChoicesComponent,
        ListChoicesComponent
    ],
    imports: [
        CommonModule,
        ElectionRoutingModule,
        MatCardModule,
        MatFormFieldModule,
        MatInputModule,
        ReactiveFormsModule,
        MatButtonModule,
        MatSelectModule,
        MatTableModule,
        MatIconModule
    ]
})
export class ElectionModule {
}
