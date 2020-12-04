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
        return this.http.post<any>(this.demUrl + 'persons/create', person);
    }

    public changePresence(person: PersonInterface): Observable<any> {
        if (person.is_present){
            return this.http.get(this.demUrl + 'persons/checkOut/' + person.id);
        }else {
            return this.http.get(this.demUrl + 'persons/checkIn/' + person.id);
        }
    }

}
