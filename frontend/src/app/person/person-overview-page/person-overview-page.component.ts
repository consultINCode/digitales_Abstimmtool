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
    public displayedColumns: string[] = ['name', 'is_present'];

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

    private changePresence(person: PersonInterface) {
        this.personService.changePresence(person).subscribe(
            (res: any) => {
                person.is_present = !person.is_present;
            }
        );
    }


}
