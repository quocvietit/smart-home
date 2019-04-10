import { PipeTransform, Pipe } from '@angular/core';
import { StringFormatPipe } from './string-format.pipe';
import { Constants } from '../utilities/constants';

@Pipe({ name: "timeChartFormat" })
export class TimeChartFormatPipe implements PipeTransform {
    constants = Constants;
    constructor(private stringFormat: StringFormatPipe){}

    transform(){

    }

    // mm:ss
    transFormDateToMinutesAndSecond(value: Date): String {
        if (!value) { return ""; }
        

        const timeValue = [
            this.formatNumber(value.getMinutes().toString()),
            this.formatNumber(value.getSeconds().toString())
        ];

        const time = this.stringFormat.transform(this.constants.TIME.LABEL_CHART, timeValue)

        return time;
    }

    // HH:mm:ss
    transFormDateToHoursAndMinutesAndSecond(value: Date): String {
        if (!value) { return ""; }
        

        const timeValue = [
            this.formatNumber(value.getHours().toString()),
            this.formatNumber(value.getMinutes().toString()),
            this.formatNumber(value.getSeconds().toString())
        ];

        const time = this.stringFormat.transform(this.constants.TIME.CURRENT_TIME, timeValue)

        return time;
    }

    transFormDateToYearAndMonthAndDay(value: Date): String {
        if (!value) { return ""; }
        


        const timeValue = [
            this.formatNumber((value.getMonth()+1).toString()),
            this.formatNumber(value.getDate().toString()),
            value.getFullYear().toString(),
        ];

        const time = this.stringFormat.transform(this.constants.TIME.CURRENT_DATE, timeValue)

        return time;
    }

    private formatNumber(value: String): String {
        return ("0" + value).substr(-2);
    }
}