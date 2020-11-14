import { Component, OnInit } from '@angular/core';
import {FormBuilder} from "@angular/forms";

@Component({
  selector: 'app-create-person-page',
  templateUrl: './create-person-page.component.html',
  styleUrls: ['./create-person-page.component.scss']
})
export class CreatePersonPageComponent implements OnInit {

  personForm = this.formBuilder.group({
        name: [''],
        is_present: [''],
      }
  )

  constructor(
      private formBuilder: FormBuilder,
  ) { }

  ngOnInit(): void {
  }

}
