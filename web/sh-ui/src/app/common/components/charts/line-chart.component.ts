import { Component, OnInit, OnChanges, OnDestroy, AfterViewInit, Input, ViewChildren, ViewChild } from '@angular/core';
import { ChartOptions } from 'chart.js';
import { Color, BaseChartDirective } from 'ng2-charts';
import * as pluginAnnotations from 'chartjs-plugin-annotation';

@Component({
    selector: 'line-chart-component',
    templateUrl: './line-chart.component.html',
    styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit, OnChanges, OnDestroy, AfterViewInit {
    @Input() lineChartData: any;
    @Input() lineChartLabels: any;

    private lineChartOptions: (ChartOptions & { annotation: any }) = {
        responsive: true,
        scales: {
            // We use this empty structure as a placeholder for dynamic theming.
            xAxes: [{
                id: 'x-axis-0',
                position: 'bottom',
                ticks: {
                    min: 0,
                    // maxRotation: 10,
                    // maxTicksLimit: 10,
                    // suggestedMax: 10
                }
            }],
            yAxes: [
                {
                    id: 'y-axis-0',
                    position: 'left',
                    ticks: {
                        beginAtZero: false,
                        fontColor: 'green',
                        min: -20,
                        max: 50
                    }
                }
                // },
                // {
                //   id: 'y-axis-1',
                //   position: 'right',
                //   gridLines: {
                //     color: 'rgba(255,0,0,0.3)',
                //   },
                //   ticks: {
                //     beginAtZero: true,
                //     fontColor: 'green',
                //     max: 100
                //   }
                // }
            ]
        },
        annotation: {
            // annotations: [
            //   {
            //     type: 'line',
            //     mode: 'vertical',
            //     scaleID: 'x-axis-0',
            //     value: 'March',
            //     borderColor: 'orange',
            //     borderWidth: 2,
            //     label: {
            //       enabled: true,
            //       fontColor: 'orange',
            //       content: 'LineAnno'
            //     }
            //   },
            // ],
        },
    };

    public lineChartColors: Color[] = [
        { // grey
            backgroundColor: 'rgba(148,159,177,0.2)',
            borderColor: 'rgba(148,159,177,1)',
            pointBackgroundColor: 'rgba(148,159,177,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(148,159,177,0.8)'
        },
        { // dark grey
            backgroundColor: 'rgba(77,83,96,0.2)',
            borderColor: 'rgba(77,83,96,1)',
            pointBackgroundColor: 'rgba(77,83,96,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(77,83,96,1)'
        },
        { // red
            backgroundColor: 'rgba(255,0,0,0.3)',
            borderColor: 'red',
            pointBackgroundColor: 'rgba(148,159,177,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(148,159,177,0.8)'
        }
    ];

    private lineChartLegend = false;
    private lineChartType = 'line';
    private lineChartPlugins = [pluginAnnotations];

    @ViewChild(BaseChartDirective) chart: BaseChartDirective;

    constructor() { }

    ngOnInit() { }

    ngOnDestroy() { }

    ngOnChanges() { }

    ngAfterViewInit() { }

    public update(){
        this.chart.update();
    }

}