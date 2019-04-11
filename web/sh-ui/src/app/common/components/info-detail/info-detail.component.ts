import {Component, OnInit, OnChanges, AfterViewInit, Input} from '@angular/core';
import { TimeChartFormatPipe } from '../../pipe/time-chart-format.pipe';
import { Constants } from '../../utilities/constants';

@Component({
    selector: 'info-detail-component',
    templateUrl: './info-detail.component.html',
    styleUrls: ['./info-detail.component.css']
})

export class InfoDetailComponent implements OnInit, OnChanges, AfterViewInit{

    constants = Constants;

    currentDate: String;
    currentTime: String;
    date: Date = new Date();
    device: String = this.constants.DEVICE.TEMPERATURE;
    deviceMeasure: String;

    @Input() currentValue: String;
    @Input() averageValue: String;
    @Input() status: String;
    @Input() isTemperature: boolean;

    constructor(
        private timeChartFormat: TimeChartFormatPipe
    ){};

    ngOnInit() {
        this.getDate();
        this.getDevice();

    };

    ngOnChanges(){
        this.getDate();
        this.getDevice();
    };

    ngAfterViewInit() {};

    setCurrentValue(currentValue: any){
        this.currentValue = currentValue;
    }

    private getDate(){
        this.date = new Date();
        this.currentDate = this.timeChartFormat.transFormDateToYearAndMonthAndDay(this.date);
        this.currentTime = this.timeChartFormat.transFormDateToHoursAndMinutesAndSecond(this.date);
    }

    private getDevice(){
        if(this.isTemperature){
            this.device = this.constants.DEVICE.TEMPERATURE;
            this.deviceMeasure = "<b>&#176;C<b>";
        }else{
            this.device = this.constants.DEVICE.HUMIDITY;
            this.deviceMeasure = "&#37;";
        }
    }
}