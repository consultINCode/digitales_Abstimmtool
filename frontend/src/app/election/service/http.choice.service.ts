import {Inject, Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {ElectionRoundInterface} from '../Interface/ElectionRound.Interface';
import {ChoiceInterface} from '../Interface/Choice.Interface';

@Injectable({
    providedIn: 'root'
})
export class HttpChoiceService {

    constructor(
        @Inject('DEM_API_URL') private demUrl: string,
        private http: HttpClient
    ) {
    }

    public getChoicesForElectionRound(electionRoundId: number): Observable<ChoiceInterface[]> {
        return this.http.get<ChoiceInterface[]>(this.demUrl + 'choice/election/' + String(electionRoundId));
    }

    public createChoice(choice: ChoiceInterface): Observable<ChoiceInterface> {
        return this.http.post<ChoiceInterface>(this.demUrl + 'choice/create', choice);
    }

}
