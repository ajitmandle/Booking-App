import { ApplicationConfig,importProvidersFrom } from '@angular/core';
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes'; 
import { provideAnimations } from '@angular/platform-browser/animations';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatListModule } from '@angular/material/list';

export const appConfig: ApplicationConfig = {
  providers: [
    provideAnimations(),
    provideRouter(routes),
    provideHttpClient(withInterceptors([])), // Add HTTP client support
    importProvidersFrom(
      MatFormFieldModule,
      MatInputModule,
      MatButtonModule,
      MatCardModule,
      MatSidenavModule,
      MatToolbarModule,
      MatListModule
    )
  ],
  
};
