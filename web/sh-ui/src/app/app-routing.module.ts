import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ChartsModule } from 'ng2-charts';
import { HomeComponent } from './home/components/home.component';
import { TemperatureComponent } from './temperature/components/temperature.component';
import { PageNotFoundComponent } from './common/components/page-not-found/page-not-found.component';
import { LineChartComponent } from './common/components/charts/line-chart.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'temperature', component: TemperatureComponent },
  { path: 'humidity', component: TemperatureComponent },
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
    PageNotFoundComponent,
    LineChartComponent
  ],
  imports: [
    ChartsModule,
    RouterModule.forRoot(
      routes
    )
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
