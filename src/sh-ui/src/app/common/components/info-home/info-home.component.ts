import {Component, OnInit, OnChanges, AfterViewInit, Input} from '@angular/core';
import { Constants } from '../../utilities/constants';
import { TimeChartFormatPipe } from '../../pipe/time-chart-format.pipe';
import { Temperature } from '../../models/temperature.model';

@Component({
    selector: 'info-home-component',
    templateUrl: './info-home.component.html',
    styleUrls: ['./info-home.component.css']
})

export class InfoHomeComponent implements OnInit, OnChanges, AfterViewInit{

    constants = Constants;

    currentDate: String;
    currentTime: String;
    date: Date = new Date();
    room: String = "PHÒNG KHÁCH";
    temperatureName: String = "Nhiệt độ";
    humidityName: String = "Độ ẩm";
    lightName: String = "Ánh sáng";
    gasName: String = "Khí GAS";
    flashLightName: String = "Bóng đèn";

    @Input() temperatureValue: String;
    @Input() humidityValue: String;
    @Input() lightValue: String;
    @Input() gasValue: String;
    @Input() flashLightValue: String;

    constructor(private timeChartFormat: TimeChartFormatPipe){};

    ngOnInit() {
        this.getDate();
    };

    ngOnChanges(){
        this.getDate();
    };

    ngAfterViewInit() {};

    private getDate(){
        this.date = new Date();
        this.currentDate = this.timeChartFormat.transFormDateToYearAndMonthAndDay(this.date);
        this.currentTime = this.timeChartFormat.transFormDateToHoursAndMinutesAndSecond(this.date);
    }
}