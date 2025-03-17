import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InventoryService {
  private apiUrl = 'http://localhost:8000/api/inventory/'; // Update with actual backend URL

  constructor(private http: HttpClient) {}

  getInventory(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
