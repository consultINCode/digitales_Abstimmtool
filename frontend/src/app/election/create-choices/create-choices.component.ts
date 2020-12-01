import {Component, EventEmitter, Input, OnChanges, OnInit, Output, SimpleChanges} from '@angular/core';
import {FormBuilder, Validators} from '@angular/forms';
import {HttpElectionRoundService} from '../service/http-election-round.service';
import {ElectionRoundInterface} from '../Interface/ElectionRound.Interface';
import {HttpChoiceService} from '../service/http.choice.service';
import {ChoiceInterface} from '../Interface/Choice.Interface';
import {Observable} from 'rxjs';

@Component({
    selector: 'app-create-choices',
    templateUrl: './create-choices.component.html',
    styleUrls: ['./create-choices.component.scss']
})
export class CreateChoicesComponent implements OnChanges, OnInit {
    @Input() electionRound: ElectionRoundInterface;
    @Output() emitCreatedChoice = new EventEmitter<ChoiceInterface>();
    public file;

    public choicesForm = this.formBuilder.group({
            description: ['', [Validators.required, Validators.minLength(3)]],
            picture: [''],
            election_round_id: ['', [Validators.required, Validators.pattern('^[0-9]*$')]],
        }
    );

    constructor(
        private formBuilder: FormBuilder,
        private httpChoiceService: HttpChoiceService
    ) {
    }

    ngOnInit(): void {
        this.choicesForm.disable();
    }

    ngOnChanges(changes: SimpleChanges): void {
        if (changes.electionRound.currentValue.id) {
            this.choicesForm.controls.election_round_id.setValue(changes.electionRound.currentValue.id);
            this.choicesForm.enable();
        }
    }

    public submitForm() {
        const choice = this.choicesForm.value as ChoiceInterface;
        this.httpChoiceService.setChoice(choice).subscribe(
            (choice: ChoiceInterface) => {
                alert('success');
                this.emitCreatedChoice.emit(choice);
                this.choicesForm.reset();
                this.choicesForm.controls.election_round_id.setValue(this.electionRound.id);
            },
            (error: any) => {
                alert('error');
            }
        );
    }
    public selectFile(event) {

        this.file = event.target.files[0];
        const myReader = new FileReader();

        myReader.onloadend = (e) => {
            this.choicesForm.controls.picture.setValue(myReader.result);
        };
        myReader.readAsDataURL(this.file);
    }
}

