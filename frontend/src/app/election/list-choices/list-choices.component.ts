import {Component, Input, OnChanges, SimpleChanges} from '@angular/core';
import {ChoiceInterface} from "../Interface/Choice.Interface";
import {MatTableDataSource} from "@angular/material/table";
import {HttpChoiceService} from "../service/http.choice.service";
import {ElectionRoundInterface} from "../Interface/ElectionRound.Interface";

@Component({
    selector: 'app-list-choices',
    templateUrl: './list-choices.component.html',
    styleUrls: ['./list-choices.component.scss']
})
export class ListChoicesComponent {

    @Input() choices: ChoiceInterface[];
    @Input() electionRound: ElectionRoundInterface;
    public displayedColumns: string[] = ['Bild', 'Beschreibung'];

}
