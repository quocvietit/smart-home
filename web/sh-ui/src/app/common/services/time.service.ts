import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TimeChartFormatPipe } from '../pipe/time-chart-format.pipe';
import { Constants } from '../utilities/constants';
import { TimeModel } from '../models/time.model';

@Injectable()
export class TimeService {
    constants = Constants;
    time: any = {};

    constructor(
        private timeChartFormat: TimeChartFormatPipe
    ) {

    }

    getCurrentTime() {
        let currentTime = new Date();
        console.log(currentTime);
        this.time.day = this.formatTime(currentTime.getDate().toString());
        this.time.month = this.formatTime(currentTime.getMonth().toString());
        this.time.year = currentTime.getFullYear().toString();
        this.time.time = this.timeChartFormat.transFormDateToHoursAndMinutesAndSecond(currentTime)
        return this.time;
    }

    getTime() {
        return new Observable(
            data => {
                setInterval(() => {
                    data.next(this.getCurrentTime())
                }, 1)
            }
        );
    }

    private formatTime(value: String): String {
        return ("0" + value).substr(-2);
    }
}