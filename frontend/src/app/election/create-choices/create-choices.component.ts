import {Component, Input, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import {FormBuilder, Validators} from "@angular/forms";
import {HttpElectionRoundService} from "../service/http-election-round.service";
import {ElectionRoundInterface} from "../Interface/ElectionRound.Interface";
import {HttpChoiceService} from "../service/http.choice.service";
import {ChoiceInterface} from "../Interface/Choice.Interface";

@Component({
    selector: 'app-create-choices',
    templateUrl: './create-choices.component.html',
    styleUrls: ['./create-choices.component.scss']
})
export class CreateChoicesComponent implements OnChanges, OnInit{
    @Input() electionRound: ElectionRoundInterface;
    public choicesForm = this.formBuilder.group({
        description: ['', [ Validators.required, Validators.minLength(3)]],
        picture: [''],
        election_round_id: [''],
        }
    );

    constructor(
        private formBuilder: FormBuilder,
        private httpChoiceService: HttpChoiceService
    ) {
    }
    ngOnInit(): void {
        this.choicesForm.disable()
    }

    ngOnChanges(changes: SimpleChanges): void {
        if(changes.electionRound.currentValue.id){
            this.choicesForm.controls['election_round_id'].setValue(changes.electionRound.currentValue.id)
            this.choicesForm.enable()
        }
    }

    public submitForm() {
        let choice = this.choicesForm.value as ChoiceInterface;
        this.httpChoiceService.setChoice(choice).subscribe(
            (succes: any) => {
                alert('success')
                this.choicesForm.reset()
            },
            (error: any) => {alert('error')}
        )

    }



}
