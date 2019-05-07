import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ChartsModule } from 'ng2-charts';
import { HomeComponent } from './home/components/home.component';
import { PageNotFoundComponent } from './common/components/page-not-found/page-not-found.component';
import { LineChartComponent } from './common/components/charts/line-chart.component';
import { AboutComponent } from './common/components/about/about.component';
import { MaterialModule } from './material.module';
import { InfoHomeComponent } from './common/components/info-home/info-home.component';
import { TitleComponent } from './common/components/title/title.component';
import { MonitorComponent } from './monitor/components/monitor.component';
import { DataTableComponent } from './common/components/data-table/data-table.component';
import { SensorInfoComponent } from './common/components/sensor-info/sensor-info.component';
import { SocketService } from './common/services/socket.service';
import { MonitorService } from './monitor/services/monitor.service';
import { TimeService } from './common/services/time.service';
import { CommonModule } from '@angular/common';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'temperature', component: MonitorComponent},
  { path: 'humidity', component: MonitorService},
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
    MonitorComponent,
    AboutComponent,
    PageNotFoundComponent,
    LineChartComponent,
    InfoHomeComponent,
    TitleComponent,
    DataTableComponent,
    SensorInfoComponent
  ],
  imports: [
    CommonModule,
    ChartsModule,
    MaterialModule,
    RouterModule.forRoot(
      routes
    )
  ],
  providers: [SocketService, MonitorService, TimeService],
  exports: [RouterModule]
})
export class AppRoutingModule { }
