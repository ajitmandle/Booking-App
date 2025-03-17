import { Component } from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatListModule } from '@angular/material/list';
import { RouterModule } from '@angular/router';
@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [MatSidenavModule, MatToolbarModule, MatListModule, RouterModule],
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.css'
})
export class SidebarComponent {

}
