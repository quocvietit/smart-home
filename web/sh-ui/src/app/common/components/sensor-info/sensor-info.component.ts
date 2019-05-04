import {Component, OnInit, OnChanges, AfterViewInit, Input} from '@angular/core';

@Component({
    selector: 'sensor-info-component',
    templateUrl: './sensor-info.component.html',
    styleUrls: ['./sensor-info.component.css']
})

export class SensorInfoComponent implements OnInit, OnChanges, AfterViewInit{
    @Input() name: any;
    @Input() status: any;

    constructor(){};

    ngOnInit() {
    };

    ngOnChanges(){};

    ngAfterViewInit() {};
}