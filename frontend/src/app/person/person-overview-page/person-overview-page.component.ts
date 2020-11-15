import {Component, OnInit} from '@angular/core';
import {PersonInterface} from '../Interface/Person.Interface';
import {HttpPersonService} from '../service/http-person.service';

@Component({
    selector: 'app-person-overview-page',
    templateUrl: './person-overview-page.component.html',
    styleUrls: ['./person-overview-page.component.scss']
})
export class PersonOverviewPageComponent implements OnInit {

    public persons: PersonInterface[];

    constructor(
        private personService: HttpPersonService
    ) {
    }

    ngOnInit(): void {
        this.getPerson();
    }

    private getPerson(): void {
        this.personService.getPersons().subscribe(
            (persons: PersonInterface[]) => {
                this.persons = persons;
            }
        );
    }

}