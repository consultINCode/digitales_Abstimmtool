import {Component, OnInit} from '@angular/core';
import {FormBuilder} from "@angular/forms";
import {PersonInterface} from "../../person/Interface/Person.Interface";

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
    ) {
    }


    public submitForm() {
        let person = this.electionForm.value as PersonInterface;
        //TODO: implement Service
    }
}
