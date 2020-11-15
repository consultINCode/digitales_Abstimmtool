import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreatePersonPageComponent } from './create-person-page.component';

describe('CreatePersonPageComponent', () => {
  let component: CreatePersonPageComponent;
  let fixture: ComponentFixture<CreatePersonPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreatePersonPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CreatePersonPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
