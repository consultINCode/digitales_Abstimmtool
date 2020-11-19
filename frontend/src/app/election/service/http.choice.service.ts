import {Inject, Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {ElectionRoundInterface} from "../Interface/ElectionRound.Interface";
import {ChoiceInterface} from "../Interface/Choice.Interface";

@Injectable({
    providedIn: 'root'
})
export class HttpChoiceService {

    constructor(
        @Inject('DEM_API_URL') private demUrl: string,
        private http: HttpClient
    ) {
    }

    public getChoicesForElectionRound(electionRoundId: number): Observable<ElectionRoundInterface[]> {
        return this.http.get<ElectionRoundInterface[]>(this.demUrl + 'electionrounds/getAllElectionRounds');
    }

    public setChoice(choice: ChoiceInterface): Observable<any> {
        return this.http.post<any>(this.demUrl + 'choice/', choice);
    }

}
