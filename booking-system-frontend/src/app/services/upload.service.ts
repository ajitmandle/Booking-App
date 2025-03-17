import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadService {
  private apiUrl = 'http://localhost:8000/api/upload/';

  constructor(private http: HttpClient) {}

  uploadFile(file: File, fileType: string): Observable<any> {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('type', fileType);

    return this.http.post(this.apiUrl, formData);
  }
}
