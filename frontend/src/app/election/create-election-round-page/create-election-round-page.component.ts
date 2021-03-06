import {Component} from '@angular/core';
import {FormBuilder} from '@angular/forms';
import {ElectionRoundInterface} from '../Interface/ElectionRound.Interface';
import {HttpElectionRoundService} from '../service/http-election-round.service';
import {ChoiceInterface} from '../Interface/Choice.Interface';

@Component({
    selector: 'app-create-election-page',
    templateUrl: './create-election-round-page.component.html',
    styleUrls: ['./create-election-round-page.component.scss']
})
export class CreateElectionRoundPageComponent {

    public isFormEnable = true;
    public createdChoices: ChoiceInterface[] = [];

    public status = [
        {value: 'not_started', name: 'nicht gestartet'},
        {value: 'running', name: 'läuft'},
        {value: 'finished', name: 'geschlossen'},
    ];

    public electionForm = this.formBuilder.group({
            id: [''],
            title: [''],
            running: [''],
            max_choices_per_person: [''],
        }
    );

    constructor(
        private formBuilder: FormBuilder,
        private httpElectionRoundService: HttpElectionRoundService
    ) {
    }


    public submitForm(): void {
        const electionRound = this.electionForm.value as ElectionRoundInterface;
        this.httpElectionRoundService.createElectionRound(electionRound).subscribe(
            (electionRoundData: ElectionRoundInterface) => {
                this.electionForm.setValue(electionRoundData);
                this.electionForm.disable();
                this.isFormEnable = false;
            },
            (error: any) => {
                alert('error');
            }
        );
    }

    public updateCreatedChoices(event: Event): void{
        // @ts-ignore
        this.createdChoices.push(event);
    }
}
