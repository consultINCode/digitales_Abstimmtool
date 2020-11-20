import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormControl} from '@angular/forms';
import {HttpPersonService} from '../service/http-person.service';
import {PersonInterface} from '../Interface/Person.Interface';

@Component({
    selector: 'app-create-person-page',
    templateUrl: './create-person-page.component.html',
    styleUrls: ['./create-person-page.component.scss']
})
export class CreatePersonPageComponent implements OnInit {

    private isPresentDefault = true;

    public personForm = this.formBuilder.group({
            name: [''],
            is_present: [this.isPresentDefault],
        }
    );

    constructor(
        private formBuilder: FormBuilder,
        private personService: HttpPersonService
    ) {
    }

    ngOnInit(): void {
    }

    public submitForm() {
        const person = this.personForm.value as PersonInterface;
        this.personService.setPerson(person).subscribe(
            (success: any) => {
                alert('success');
            },
            (error: any) => {
                alert('error');
            }
        );
    }
}

