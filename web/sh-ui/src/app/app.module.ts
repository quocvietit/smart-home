import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA, NO_ERRORS_SCHEMA } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { ChartsModule } from 'ng2-charts';

import { MatTabsModule } from '@angular/material/tabs';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

import { CategoryComponent } from './common/components/category/category.component';
import { StringFormatPipe } from './common/pipe/string-format.pipe';
import { TimeChartFormatPipe } from './common/pipe/time-chart-format.pipe';
import { AnalyticsService } from './common/services/analytics.service';


@NgModule({
  declarations: [
    AppComponent,
    CategoryComponent,
    StringFormatPipe,
    TimeChartFormatPipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ChartsModule,
    MatTabsModule,
    BrowserAnimationsModule
  ],
  entryComponents: [CategoryComponent],
  providers: [
    StringFormatPipe,
    TimeChartFormatPipe,
    AnalyticsService
  ],
  bootstrap: [AppComponent, CategoryComponent],
  schemas: [
    CUSTOM_ELEMENTS_SCHEMA,
    NO_ERRORS_SCHEMA
  ]
})

export class AppModule {
  links = [
    {
      path: '/home',
      label: 'Home'

    }
  ]
}


