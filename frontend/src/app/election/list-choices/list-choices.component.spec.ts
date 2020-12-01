import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListChoicesComponent } from './list-choices.component';

describe('ListChoicesComponent', () => {
  let component: ListChoicesComponent;
  let fixture: ComponentFixture<ListChoicesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListChoicesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListChoicesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
