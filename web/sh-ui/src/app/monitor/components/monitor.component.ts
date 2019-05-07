import { Component, OnInit, OnChanges, AfterViewInit, ViewChild } from '@angular/core';

import { ChartDataSets, ChartOptions } from 'chart.js';
import { Label } from 'ng2-charts';

import { LineChartComponent } from '../../common/components/charts/line-chart.component';
import { StringFormatPipe } from '../../common/pipe/string-format.pipe';
import { TimeChartFormatPipe } from '../../common/pipe/time-chart-format.pipe';
import { AnalyticsService } from '../../common/services/analytics.service';
import { Observable } from 'rxjs';
import { MonitorService } from '../services/monitor.service';
import { Constants } from 'src/app/common/utilities/constants';
import { TimeService } from 'src/app/common/services/time.service';
import { TimeModel } from 'src/app/common/models/time.model';

@Component({
    selector: 'monitor-component',
    templateUrl: './monitor.component.html',
    styleUrls: ['./monitor.component.css']
})

export class MonitorComponent implements OnInit, OnChanges, AfterViewInit {
    @ViewChild("LineChartComponent") chart: LineChartComponent;

    constants = Constants;

    currentTime: String;
    isLight: boolean = false;
    isGas: boolean = false;

    chartData: ChartDataSets[] = [
        { data: [17, 20, 21, 25, 26, 26, 26, 26, 26, 26], label: 'Temperature' },
    ];
    chartLabels: Label[] = ['22.10', '22.11', '22.12', '22.13', '22.14', '22.15', '22.16', '22.17', '22.18', '22.19'];

    data = this.chartData[0].data as number[];
    currentTemperature = this.chartData[0].data[9].toString();
    averageTemperature = this.analyticService.calAverage(this.chartData[0].data);
    statusTemperature = "Bình Thường";

    temperature: Observable<String>;



    constructor(
        private stringFormat: StringFormatPipe,
        private timeChartFormat: TimeChartFormatPipe,
        private analyticService: AnalyticsService,
        private service: MonitorService,
        private timeService: TimeService
    ) {
        this.getDate();
    }

    ngOnInit() {
        this.service.getMessage().subscribe(data => {
            console.log("Value");
            this.currentTemperature = data.toString();
            this.chartLabels.shift();
            this.chartLabels.push(this.timeChartFormat.transFormDateToHoursAndMinutesAndSecond(new Date()).toString());
            this.data.shift();
            this.data.push(Number(this.currentTemperature));
            this.averageTemperature = this.analyticService.calAverage(this.chartData[0].data as number[]);
        }, err => {
            console.log("err: " + err);
        });
    }

    ngOnChanges() {

    }

    ngAfterViewInit() { }

    getDate() {
        this.timeService.getTime().subscribe(
            data => {
                let time = data as TimeModel;
                this.currentTime = time.time;
            },
            err => {
                console.log("Get time error: " + err);
            }
        );
    }

    controllLight(){
        console.log("Turn light");
        this.isLight = !this.isLight;
        this.isGas = !this.isGas;
    }

    public randomize(): void {
        for (let i = 0; i < this.chartData.length; i++) {
            for (let j = 0; j < this.chartData[i].data.length; j++) {
                this.chartData[i].data[j] = this.generateNumber(i);
            }
        }
        //this.chart.update();
    }

    private generateNumber(i: number) {
        return Math.floor((Math.random() * (i < 2 ? 10 : 100)) + 1);
    }

    // events
    public chartClicked({ event, active }: { event: MouseEvent, active: {}[] }): void {
        console.log(event, active);
    }

    public chartHovered({ event, active }: { event: MouseEvent, active: {}[] }): void {
        console.log(event, active);
    }


    public pushOne() {
        this.chartLabels.shift();
        this.chartLabels.push(this.timeChartFormat.transFormDateToHoursAndMinutesAndSecond(new Date()).toString());
        this.chartData.forEach((x, i) => {
            const num = this.generateNumber(i);
            const data: number[] = x.data as number[];
            data.shift();
            data.push(num);
        });
        this.averageTemperature = this.analyticService.calAverage(this.chartData[0].data as number[]);
        this.currentTemperature = this.chartData[0].data[9].toString();

        // this.chart.update();

    }

    public changeLabel() {
        this.chartLabels[2] = ['1st Line', '2nd Line'];
        //this.chart.update();
    }

}

