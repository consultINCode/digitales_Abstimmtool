import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateElectionRoundPageComponent } from './create-election-round-page.component';

describe('CreateElectionPageComponent', () => {
  let component: CreateElectionRoundPageComponent;
  let fixture: ComponentFixture<CreateElectionRoundPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateElectionRoundPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateElectionRoundPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
