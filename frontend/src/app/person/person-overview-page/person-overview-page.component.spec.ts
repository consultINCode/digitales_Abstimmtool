import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PersonOverviewPageComponent } from './person-overview-page.component';

describe('PersonOverviewPageComponent', () => {
  let component: PersonOverviewPageComponent;
  let fixture: ComponentFixture<PersonOverviewPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PersonOverviewPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PersonOverviewPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
