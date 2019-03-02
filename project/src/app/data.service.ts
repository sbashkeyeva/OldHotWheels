import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  firstClick(){
    return console.log('clicked')
  }
  constructor() { }
}
