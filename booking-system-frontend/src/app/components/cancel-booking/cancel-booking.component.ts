import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { BookingService } from '../../services/booking.service';
import { ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-cancel-booking',
  standalone: true,
  templateUrl: './cancel-booking.component.html',
  styleUrls: ['./cancel-booking.component.css'],
  imports: [CommonModule,MatCardModule,ReactiveFormsModule,MatFormFieldModule,MatSelectModule,MatButtonModule],
})
export class CancelBookingComponent implements OnInit {
  cancelForm!: FormGroup;
  bookings: any[] = []; // Store existing bookings

  constructor(
    private fb: FormBuilder,
    private bookingService: BookingService,
    private snackBar: MatSnackBar
  ) {}

  ngOnInit() {
    this.cancelForm = this.fb.group({
      booking_id: ['', Validators.required],
    });

    // Fetch existing bookings
    this.bookingService.getBookings().subscribe((data) => {
      this.bookings = data;
      console.log(this.bookings)
    });
  }

  cancelBooking() {
    if (this.cancelForm.invalid) return;

    const bookingId = this.cancelForm.value.booking_id;

    this.bookingService.cancelBooking(bookingId).subscribe(
      (response) => {
        this.snackBar.open('Booking canceled successfully', 'Close', {
          duration: 3000,
          panelClass: ['success-snackbar'],
        });

        // Remove booking from dropdown
        this.bookings = this.bookings.filter((b) => b.id !== bookingId);
      },
      (error) => {
        this.snackBar.open('Error canceling booking', 'Close', {
          duration: 3000,
          panelClass: ['error-snackbar'],
        });
      }
    );
  }
}
