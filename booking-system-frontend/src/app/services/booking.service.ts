import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BookingService {
  private apiUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) {}

  bookItem(memberId: number, inventoryId: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/book/`, { member_id: memberId, inventory_id: inventoryId });
  }

  cancelBooking(bookingId: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/cancel/`, { booking_id: bookingId });
  }
  getMembers(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/members/`);
  }

  getInventory(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/inventory/`);
  }
  getBookings(): Observable<any> {
    return this.http.get(`${this.apiUrl}/bookings/`);
  }
}
