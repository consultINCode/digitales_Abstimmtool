import {Component, Input} from '@angular/core';
import {ChoiceInterface} from '../Interface/Choice.Interface';
import {ElectionRoundInterface} from '../Interface/ElectionRound.Interface';

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
