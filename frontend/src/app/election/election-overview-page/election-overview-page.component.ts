import {Component, OnInit} from '@angular/core';
import {ElectionRoundInterface} from '../Interface/ElectionRound.Interface';
import {HttpElectionRoundService} from '../service/http-election-round.service';

@Component({
    selector: 'app-election-overview-page',
    templateUrl: './election-overview-page.component.html',
    styleUrls: ['./election-overview-page.component.scss']
})
export class ElectionOverviewPageComponent implements OnInit {

    public electionRounds: ElectionRoundInterface[];
    public displayedColumns: string[] = ['title', 'running', 'max_choices_per_person'];

    public status = {
        running: 'play_arrow',
        finished: 'stop',
        not_started: 'not_started'
    }

    constructor(
        private httpElectionRoundService: HttpElectionRoundService
    ) {
    }

    ngOnInit(): void {
        this.getAllElectionRounds();
    }

    private getAllElectionRounds(): void {

        this.httpElectionRoundService.getElectionRounds().subscribe(
            (electionRound: ElectionRoundInterface[]) => {
                this.electionRounds = electionRound;
            }
        );
    }

}
