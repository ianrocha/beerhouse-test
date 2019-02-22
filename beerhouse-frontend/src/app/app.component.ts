import { Component, OnInit } from '@angular/core';

import { ApiService } from './api.service';
import { BeerhouseItem } from './beerhouse.interface';

@Component({
  selector: 'app-root',
  templateUrl: 'beerhouse.component.html',
})
export class AppComponent implements OnInit {

  items: BeerhouseItem[];
  error: any;
  item: BeerhouseItem;

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.api.getBeerhouseItems().subscribe(
      (items: BeerhouseItem[]) => this.items = items,
      (error: any) => this.error = error
    );
  }

  detail(id: number) {
    this.api.getBeerhouseItemDetail(id).subscribe(
      (item: BeerhouseItem) => this.item = item,
      (error: any) => this.error = error
    );
  }

  add(itemName: string, itemDescription: string, itemHarmonization: string,
  itemColor: string, itemAlcoholContent: string, itemTemperature: string,
  itemIngredients: string, itemImage: File) {
    this.api.createBeerhouseItem(itemName, itemDescription, itemHarmonization,
    itemColor, itemAlcoholContent, itemTemperature, itemIngredients, itemImage).subscribe(
      (item: BeerhouseItem) => this.items.push(item)
    );
  }

  delete(id: number) {
    this.api.deleteBeerhouseItem(id).subscribe(
      (success: any) => this.items.splice(
        this.items.findIndex(item => item.id === id)
      )
    );
  }
}
