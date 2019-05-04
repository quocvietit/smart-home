import { Component, OnInit, OnChanges, AfterViewInit, ViewChild } from '@angular/core';
import { StringFormatPipe } from '../../common/pipe/string-format.pipe';
import { TimeChartFormatPipe } from '../../common/pipe/time-chart-format.pipe';
import { AnalyticsService } from '../../common/services/analytics.service';
import { LineChartComponent } from '../../common/components/charts/line-chart.component';
import { ChartDataSets } from 'chart.js';
import { Label } from 'ng2-charts';
import { InfoHomeComponent } from '../../common/components/info-home/info-home.component';
import { DataTableComponent } from 'src/app/common/components/data-table/data-table.component';
import { initDomAdapter } from '@angular/platform-browser/src/browser';
import { SocketService } from 'src/app/common/services/socket.service';
import { Observable } from 'rxjs';
import { TemperatureService } from 'src/app/temperature/services/temperature.service';

@Component({
    selector: 'home-component',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit, OnChanges, AfterViewInit {

    @ViewChild("InfoHomeComponent") infoHome: InfoHomeComponent;

    currentDate: String;
    currentTime: String;

    temperature: String;
    humidity: String;
    light: String;
    gas: String;
    flashLight: String;


    constructor(
        private stringFormat: StringFormatPipe,
        private timeChartFormat: TimeChartFormatPipe,
        private analyticService: AnalyticsService,
        private socketService: TemperatureService

    ) {
        setInterval(() => {
            this.getDate();
        }, 1);
    }

    ngOnInit() {
        this.init();
        this.getDate();
    }

    ngOnChanges() {
        this.getDate();
    }

    ngAfterViewInit() { }
    
    init(){
        console.log("ahihi ")
        this.socketService.getMessage().subscribe(
            data =>{
                this.temperature = data.toString();
                console.log(this.temperature);
            },
            err => {
                console.log("err: " + err);
            }
        );
    }

    getDate() {
        let time = new Date();
        this.currentTime = this.timeChartFormat.transFormDateToHoursAndMinutesAndSecond(time);
        this.currentDate = this.timeChartFormat.transFormDateToYearAndMonthAndDay(time)
    }

}