import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class ApiService {

  private apiRoot = 'http://localhost:8000/';

  constructor(private http: HttpClient) { }


  getBeerhouseItems() {
    return this.http.get(this.apiRoot.concat('beer/'));
  }

  getBeerhouseItemDetail(id: number) {
    return this.http.get(this.apiRoot.concat('beer/' + id + '/'));
  }

  createBeerhouseItem(name: string, description: string, harmonization: string, color: string, alcohol_content: string, temperature: string, ingredients: string, image: File) {
    return this.http.post(
      this.apiRoot.concat('beer/'),
      { name, description, harmonization, color, alcohol_content, temperature, ingredients, image }
    );
  }

  putBeerhouseItem(id: number, name: string, description: string, harmonization: string, color: string, alcohol_content: string, temperature: string, ingredients: string, image: File) {
    return this.http.put(
      this.apiRoot.concat('beer/' + id + '/'),
      { name, description, harmonization, color, alcohol_content, temperature, ingredients, image }
    );
  }

  deleteBeerhouseItem(id: number) {
    return this.http.delete(this.apiRoot.concat('beer/' + id + '/'));
  }
}
