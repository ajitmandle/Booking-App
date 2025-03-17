import { Routes } from '@angular/router';
import { BookingComponent } from './components/booking/booking.component';
import { InventoryComponent } from './components/inventory/inventory.component';
import { UploadComponent } from './components/upload/upload.component';
import { CancelBookingComponent } from './components/cancel-booking/cancel-booking.component';


export const routes: Routes = [
  { path: '', redirectTo: '/booking', pathMatch: 'full' }, // Default route
  { path: 'booking', component: BookingComponent }, // Booking component route
  { path: 'inventory', component: InventoryComponent },
  { path: 'upload', component: UploadComponent },
  { path: 'cancel-booking', component: CancelBookingComponent },
];
