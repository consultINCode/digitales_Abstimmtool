import {Inject, Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {ElectionRoundInterface} from "../Interface/ElectionRound.Interface";

@Injectable({
  providedIn: 'root'
})
export class HttpElectionRoundService {

  constructor(
      @Inject('DEM_API_URL') private demUrl: string,
      private http: HttpClient
  ) {}

  public getElectionRounds(): Observable<ElectionRoundInterface[]> {
    return this.http.get<ElectionRoundInterface[]>(this.demUrl + 'electionrounds/getAllElectionRounds');
  }

  public setElectionRound(electionRound: ElectionRoundInterface): Observable<ElectionRoundInterface> {
    return this.http.post<ElectionRoundInterface>(this.demUrl + 'electionrounds/createElectionRound', electionRound);
  }

}
