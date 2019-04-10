import {Component, OnInit, OnChanges, AfterViewInit, ViewChild} from '@angular/core';
import { StringFormatPipe } from '../../common/pipe/string-format.pipe';
import { TimeChartFormatPipe } from '../../common/pipe/time-chart-format.pipe';
import { AnalyticsService } from '../../common/services/analytics.service';
import { LineChartComponent } from '../../common/components/charts/line-chart.component';
import { ChartDataSets } from 'chart.js';
import { Label } from 'ng2-charts';

@Component({
    selector: 'home-component',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit, OnChanges, AfterViewInit{
    chartData: ChartDataSets[] = [
        { data: [17, 20, 21, 25, 26, 26, 26, 26, 26, 26], label: 'Temperature' },
        { data: [17, 20, 21, 25, 26, 26, 26, 26, 26, 26], label: 'Humidity' },
    ];
    chartLabels: Label[] = ['22.10', '22.11', '22.12', '22.13', '22.14', '22.15', '22.16', '22.17', '22.18', '22.19'];

    currentDate = this.timeChartFormat.transFormDateToYearAndMonthAndDay(new Date());
    currentTime = this.timeChartFormat.transFormDateToMinutesAndSecond(new Date());
    currentTemperature = this.chartData[0].data[9];
    averageTemperature = this.analyticService.calAverage(this.chartData[0].data);

    @ViewChild("LineChartComponent") chart: LineChartComponent;

    constructor(
        private stringFormat: StringFormatPipe,
        private timeChartFormat: TimeChartFormatPipe,
        private analyticService: AnalyticsService
    ) { }

    ngOnInit() {
    }

    ngOnChanges(){

    }

    ngAfterViewInit(){}

    public randomize(): void {
        for (let i = 0; i < this.chartData.length; i++) {
            for (let j = 0; j < this.chartData[i].data.length; j++) {
                this.chartData[i].data[j] = this.generateNumber(i);
            }
        }
        this.chart.update();
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
        this.currentDate = this.timeChartFormat.transFormDateToYearAndMonthAndDay(new Date());
        this.currentTime = this.timeChartFormat.transFormDateToHoursAndMinutesAndSecond(new Date());
        this.chartLabels.shift();
        this.chartLabels.push(this.timeChartFormat.transFormDateToHoursAndMinutesAndSecond(new Date()).toString());
        this.chartData.forEach((x, i) => {
            const num = this.generateNumber(i);
            const data: number[] = x.data as number[];
            data.shift();
            data.push(num);
        });
        this.averageTemperature = this.analyticService.calAverage(this.chartData[0].data as number[]);
        this.currentTemperature = this.chartData[0].data[9];
        this.chart.update();

    }

    public changeLabel() {
        this.chartLabels[2] = ['1st Line', '2nd Line'];
        this.chart.update();
    }
}