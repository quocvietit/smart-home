import { Component, OnInit, OnChanges, AfterViewInit, ViewChild } from '@angular/core';

import { ChartDataSets, ChartOptions } from 'chart.js';
import { Label, Color } from 'ng2-charts';

import { LineChartComponent } from '../../common/components/charts/line-chart.component';
import { StringFormatPipe } from '../../common/pipe/string-format.pipe';
import { TimeChartFormatPipe } from '../../common/pipe/time-chart-format.pipe';
import { Observable } from 'rxjs';
import { MonitorService } from '../services/monitor.service';
import { Constants } from 'src/app/common/utilities/constants';
import { TimeService } from 'src/app/common/services/time.service';
import { TimeModel } from 'src/app/common/models/time.model';
import { DeviceService } from 'src/app/common/services/device.service';
import { SocketService } from 'src/app/common/services/socket.service';

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

    temperatureChartOptions: (ChartOptions & { annotation: any });
    temperatureLineChartColor: Color[];
    temperatureData: ChartDataSets[];
    temperatureLabels: Label[] = [];


    humidityChartOptions: (ChartOptions & { annotation: any });
    humidityLineChartColor: Color[];
    humidityData: ChartDataSets[] = [];
    humidityLabels: Label[] = [];

    statusTemperature = "Bình Thường";

    temperature: Observable<String>;

    constructor(
        private stringFormat: StringFormatPipe,
        private timeChartFormat: TimeChartFormatPipe,
        private monitorService: MonitorService,
        private timeService: TimeService,
        private deviceService: DeviceService,
        private socketService: SocketService
    ) {
        this.configChart();
        this.getDate();
    }

    ngOnInit() {
        this.initData();
        this.initSocket();
    }

    ngOnChanges() {

    }

    ngAfterViewInit() {

     }

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

    configChart() {
        this.temperatureChartOptions = {
            responsive: false,
            spanGaps: true,
            scales: {
                // We use this empty structure as a placeholder for dynamic theming.
                xAxes: [{
                    id: 'x-axis-0',
                    position: 'bottom',
                    gridLines: {
                        zeroLineColor: "transparent"
                    },
                    ticks: {
                        min: 0,
                        maxRotation: 10,
                        maxTicksLimit: 10,
                        suggestedMax: 10,
                        padding: 10,
                        fontColor: "rgb(61, 61, 62)",
                        fontStyle: "bold"
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "Biểu đồ nhiệt độ thời gian thực"
                    }
                }],
                yAxes: [
                    {
                        id: 'y-axis-0',
                        position: 'left',
                        ticks: {
                            beginAtZero: false,
                            min: -20,
                            max: 100,
                            padding: 10,
                            fontColor: 'rgb(61, 61, 62)',
                            fontStyle: "bold"
                        },
                        scaleLabel: {
                            display: true,
                            labelString: "C"
                        },
                        stacked: true
                    }
                ]
            },
            annotation: {
            },
        };

        this.temperatureLineChartColor = [
            { // grey
                backgroundColor: 'green',
                borderColor: 'black',
                pointBackgroundColor: '#80B6F4',
                pointBorderColor: '#80B6F4',
                pointHoverBackgroundColor: '#80B6F4',
                pointHoverBorderColor: 'rgba(148,159,177,0.8)',
                pointBorderWidth: 2,
                pointHoverRadius: 10,
                pointHoverBorderWidth: 1,
                pointRadius: 3,
                borderWidth: 4,
            }
        ];

        this.humidityChartOptions = {
            responsive: false,
            spanGaps: true,
            scales: {
                // We use this empty structure as a placeholder for dynamic theming.
                xAxes: [{
                    id: 'x-axis-0',
                    position: 'bottom',
                    gridLines: {
                        zeroLineColor: "transparent"
                    },
                    ticks: {
                        min: 0,
                        maxRotation: 10,
                        maxTicksLimit: 10,
                        suggestedMax: 10,
                        padding: 10,
                        fontColor: "rgb(61, 61, 62)",
                        fontStyle: "bold"
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "Biểu đồ độ ẩm thời gian thực"
                    }
                }],
                yAxes: [
                    {
                        id: 'y-axis-0',
                        position: 'left',
                        ticks: {
                            beginAtZero: true,
                            min: 0,
                            max: 100,
                            padding: 10,
                            fontColor: 'rgb(61, 61, 62)',
                            fontStyle: "bold"
                        },
                        scaleLabel: {
                            display: true,
                            labelString: "%"
                        }
                    }
                ]
            },
            annotation: {
            },
        };


        this.humidityLineChartColor = [
            { // dark grey
                backgroundColor: 'rgba(77,83,96,0.2)',
                borderColor: 'rgba(77,83,96,1)',
                pointBackgroundColor: '#80B6F4',
                pointBorderColor: '#80B6F4',
                pointHoverBackgroundColor: '#80B6F4',
                pointHoverBorderColor: 'rgba(148,159,177,0.8)',
                pointBorderWidth: 2,
                pointHoverRadius: 10,
                pointHoverBorderWidth: 1,
                pointRadius: 3,
                borderWidth: 4,
            }
        ];
    }

    initData(){
        this.temperatureData = [
            { 
                data: this.monitorService.temperatureData, 
                label: this.constants.DEVICE.TEMPERATURE ,
                fill: "start"
            },
        ];
        this.temperatureLabels = this.monitorService.temperatureLabel;

        this.humidityData = [
            { 
                data: this.monitorService.humidityData, 
                label: this.constants.DEVICE.TEMPERATURE,
                fill: "start"
            },
        ];
        this.humidityLabels = this.monitorService.humidityLabel;

        this.isLight = this.monitorService.isLight;
        this.isGas = this.monitorService.isGas;
       
    }

    initSocket(){
        this.socketService.getMessage("temperature").subscribe(data => {
            this.monitorService.temperatureData.push(data);
            this.monitorService.temperatureData.shift();
            this.temperatureLabels.push(this.currentTime.toString());
            this.temperatureLabels.shift();
        }, err => {
            console.log("err: " + err);
        });

        this.socketService.getMessage("humidity").subscribe(data => {
            this.monitorService.humidityData.push(data);
            this.monitorService.humidityData.shift();
            this.humidityLabels.push(this.currentTime.toString());
            this.humidityLabels.shift();
        }, err => {
            console.log("err: " + err);
        });

        this.socketService.getMessage("gas").subscribe(data => {
            let value = data as number;
            this.isGas = value == 1? true: false;
        }, err => {
            console.log("err: " + err);
        });

        this.socketService.getMessage("flashLight").subscribe(data => {
            let value = data as number;
            this.isLight = value == 1? true: false;
        }, err => {
            console.log("err: " + err);
        });
    }

    controllLight() {
        this.deviceService.controlLight(this.isLight).toPromise().then(
            data => {

            }
        );
        this.isLight = !this.isLight;

    }

    // events
    public chartClicked({ event, active }: { event: MouseEvent, active: {}[] }): void {
        console.log(event, active);
    }

    public chartHovered({ event, active }: { event: MouseEvent, active: {}[] }): void {
        console.log(event, active);
    }
}

