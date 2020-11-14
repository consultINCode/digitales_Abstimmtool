import { TestBed } from '@angular/core/testing';

import { HttpPersonService } from './http-person.service';

describe('HttpPersonService', () => {
  let service: HttpPersonService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HttpPersonService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
