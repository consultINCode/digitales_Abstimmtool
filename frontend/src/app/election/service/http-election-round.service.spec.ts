import { TestBed } from '@angular/core/testing';

import { HttpElectionRoundService } from './http-election-round.service';

describe('HttpElectionRoundService', () => {
  let service: HttpElectionRoundService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HttpElectionRoundService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
