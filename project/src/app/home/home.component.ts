import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(private data:DataService) { }
  h1Style:boolean=false
  ngOnInit() {
  }
  firstClick(){
    // console.log('clicked')
    this.data.firstClick();
  }

}
