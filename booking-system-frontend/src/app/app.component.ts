import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SidebarComponent } from './components/sidebar/sidebar.component'; 
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [SidebarComponent], // Import your BookingComponent
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'booking-system';
}
