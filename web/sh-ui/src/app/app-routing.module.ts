import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ChartsModule } from 'ng2-charts';
import { HomeComponent } from './home/components/home.component';
import { TemperatureComponent } from './temperature/components/temperature.component';
import { PageNotFoundComponent } from './common/components/page-not-found/page-not-found.component';
import { LineChartComponent } from './common/components/charts/line-chart.component';
import { InfoDetailComponent } from './common/components/info-detail/info-detail.component';
import { HumidityComponent } from './humidity/components/humidity.component';
import { AboutComponent } from './common/components/about/about.component';
import { MaterialModule } from './material.module';
import { InfoHomeComponent } from './common/components/info-home/info-home.component';
import { TitleComponent } from './common/components/title/title.component';
import { MonitorComponent } from './monitor/components/monitor.component';
import { TemperatureService } from './temperature/services/temperature.service';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'temperature', component: TemperatureComponent },
  { path: 'humidity', component: HumidityComponent },
  { path: 'monitor', component: MonitorComponent},
  { path: 'about', component: AboutComponent},
  { path: '404', component: PageNotFoundComponent},
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  },
  { path: '**', component: PageNotFoundComponent }
];

@NgModule({
  declarations: [
    HomeComponent,
    TemperatureComponent,
    HumidityComponent,
    MonitorComponent,
    AboutComponent,
    PageNotFoundComponent,
    LineChartComponent,
    InfoDetailComponent,
    InfoHomeComponent,
    TitleComponent
  ],
  imports: [
    ChartsModule,
    MaterialModule,
    RouterModule.forRoot(
      routes
    )
  ],
  providers: [TemperatureService],
  exports: [RouterModule]
})
export class AppRoutingModule { }
