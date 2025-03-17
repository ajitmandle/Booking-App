import { Component, OnInit } from '@angular/core';
import { BookingService } from '../../services/booking.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
@Component({
  selector: 'app-booking',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatFormFieldModule,
    MatSelectModule,
    MatButtonModule,
    MatCardModule 
  ],
  templateUrl: './booking.component.html',
  styleUrls: ['./booking.component.css']
})
export class BookingComponent implements OnInit {
  members: any[] = [];
  inventory: any[] = [];
  selectedMemberId!: number;
  selectedInventoryId!: number;

  constructor(private bookingService: BookingService) {}

  ngOnInit() {
    this.loadMembers();
    this.loadInventory();
  }

  loadMembers() {
    this.bookingService.getMembers().subscribe(data => {
      this.members = data;
    });
  }

  loadInventory() {
    this.bookingService.getInventory().subscribe(data => {
      this.inventory = data;
    });
  }

  submitBooking() {
    this.bookingService.bookItem(this.selectedMemberId, this.selectedInventoryId).subscribe({
      next: (value) =>{
      if (value.error==undefined)
      {
        alert('booked')
      }
      else
      {
        alert(value.error)
      }
      },
      error: err => alert(err.error),
    });
  }
}
