import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateChoicesComponent } from './create-choices.component';

describe('CreateChoicesComponent', () => {
  let component: CreateChoicesComponent;
  let fixture: ComponentFixture<CreateChoicesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateChoicesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateChoicesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
