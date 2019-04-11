import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA, NO_ERRORS_SCHEMA } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { CategoryComponent } from './common/components/category/category.component';
import { StringFormatPipe } from './common/pipe/string-format.pipe';
import { TimeChartFormatPipe } from './common/pipe/time-chart-format.pipe';
import { AnalyticsService } from './common/services/analytics.service';
import { MaterialModule } from './material.module';


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
    BrowserAnimationsModule,
    MaterialModule
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
}


