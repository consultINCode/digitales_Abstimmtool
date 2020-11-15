import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ElectionOverviewPageComponent } from './election-overview-page.component';

describe('ElectionOverviewPageComponent', () => {
  let component: ElectionOverviewPageComponent;
  let fixture: ComponentFixture<ElectionOverviewPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ElectionOverviewPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ElectionOverviewPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
