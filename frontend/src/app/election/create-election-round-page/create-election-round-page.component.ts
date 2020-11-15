import {Component} from '@angular/core';
import {FormBuilder} from "@angular/forms";
import {ElectionRoundInterface} from "../Interface/ElectionRound.Interface";
import {HttpElectionRoundService} from "../service/http-election-round.service";

@Component({
    selector: 'app-create-election-page',
    templateUrl: './create-election-round-page.component.html',
    styleUrls: ['./create-election-round-page.component.scss']
})
export class CreateElectionRoundPageComponent {

    public status = [
        {value:'depending' ,name: 'haltend'},
        {value:'running' ,name: 'läuft'},
        {value:'closed' ,name: 'geschlossen'},
    ]

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


    public submitForm() {
        let electionRound = this.electionForm.value as ElectionRoundInterface;
        this.httpElectionRoundService.setElectionRound(electionRound).subscribe(
            (success: any) => {
                alert('success');
            },
            (error: any) => {
                alert('error');
            }
        );
    }
}
