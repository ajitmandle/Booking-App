import { Component } from '@angular/core';
import { UploadService } from '../../services/upload.service';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatButtonModule,
    MatFormFieldModule,
    MatSelectModule
  ],
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent {
  selectedFile: File | null = null;
  selectedType: string = 'members'; // Default selection

  constructor(private uploadService: UploadService) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  uploadFile() {
    if (!this.selectedFile) {
      alert("Please select a file first!");
      return;
    }

    this.uploadService.uploadFile(this.selectedFile, this.selectedType).subscribe({
      next: (response) => alert("File uploaded successfully!"),
      error: (error) => alert("File upload failed!")
    });
  }
}
