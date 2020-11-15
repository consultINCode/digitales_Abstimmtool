import {Inject, Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {PersonInterface} from '../Interface/Person.Interface';
import {Observable} from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class HttpPersonService {

    constructor(
        @Inject('DEM_API_URL') private demUrl: string,
        private http: HttpClient
    ) {
    }

    public getPersons(): Observable<PersonInterface[]> {
        return this.http.get<PersonInterface[]>(this.demUrl + 'persons/getAllPersons');
    }

    public setPerson(person: PersonInterface): Observable<any> {
        return this.http.post<any>(this.demUrl + 'persons/createPerson', person);
    }

}
