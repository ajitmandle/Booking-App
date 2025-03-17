import { Component, OnInit,ViewChild } from '@angular/core';
import { InventoryService } from '../../services/inventory.service';
import { CommonModule } from '@angular/common';
import { MatTableModule } from '@angular/material/table';
import { MatCardModule } from '@angular/material/card';
import {MatPaginator, MatPaginatorModule} from '@angular/material/paginator';
import {MatSort, MatSortModule, SortDirection} from '@angular/material/sort';
@Component({
  selector: 'app-inventory',
  standalone: true,
  imports: [
    CommonModule,
    MatTableModule,
    MatCardModule,
    MatPaginatorModule,
    MatSortModule
  ],
  templateUrl: './inventory.component.html',
  styleUrls: ['./inventory.component.css']
})
export class InventoryComponent implements OnInit {
  inventory: any[] = [];
  displayedColumns: string[] = ['description', 'title', 'remaining_count','expiration_date'];
  // @ViewChild(MatPaginator) paginator: MatPaginator;
  // @ViewChild(MatSort) sort: MatSort;


  constructor(private inventoryService: InventoryService) {}

  ngOnInit() {
    this.loadInventory();
  }

  loadInventory() {
    this.inventoryService.getInventory().subscribe(data => {
      this.inventory = data;
    });
  }
}
