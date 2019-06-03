import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { TimeModel } from '../models/time.model';
import { Temperature } from '../models/temperature.model';
import { Device } from '../models/device.model';

@Injectable()
export class DeviceService {
    uri: string = 'localhost'
    constructor(private http: HttpClient) { }

    getValue(id: number) {
        return this.http.get("http://"+this.uri+":8888/device-status/" + id)
            .pipe(map(item => new Device(item)));
    }

    getValueForChart(id: number) {
        return this.http.get("http://"+this.uri+":8888/device-status/chart/" + id)
            .pipe(map(this.extractData));
    }

    controlLight(isLight: boolean) {
        console.log(isLight);
        if (isLight) {
            console.log(isLight);
            return this.http.get("http://"+this.uri+":8888/device/flash-light/control/off").pipe(map(this.extractData));
        } else {
            return this.http.get("http://"+this.uri+":8888/device/flash-light/control/on").pipe(map(this.extractData));
        }
    }

    getAnalytic(time: number){
        return this.http.get("http://"+this.uri+":8888/device-status/analytic/"+time).pipe(map(this.extractData));;
    }

    private extractData(res: Response) {
        let body = res;
        return body || {};
    }
}

