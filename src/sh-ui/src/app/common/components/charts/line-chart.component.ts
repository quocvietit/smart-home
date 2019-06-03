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
    @Input() lineChartOptions: any;
    @Input() lineChartColors: any;

    private lineChartLegend = true;
    private lineChartType = 'line';
    private lineChartPlugins = [pluginAnnotations];

    @ViewChild(BaseChartDirective) chart: BaseChartDirective;

    constructor() { }

    ngOnInit() { }

    ngOnDestroy() { }

    ngOnChanges() { }

    ngAfterViewInit() { }

    public update() {
        this.chart.update();
    }

    public chartClicked({ event, active }: { event: MouseEvent, active: {}[] }): void {
        //console.log(event, active);
    }

    public chartHovered({ event, active }: { event: MouseEvent, active: {}[] }): void {
        //console.log(event, active);
    }
}