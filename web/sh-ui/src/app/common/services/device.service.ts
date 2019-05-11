import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable()
export class DeviceService {
    constructor(private http: HttpClient) { }

    getValue(id: number) {
        return this.http.get("http://localhost:8888/device-status/" + id)
            .pipe(map(this.extractData));
    }

    getValueForChart(id: number) {
        return this.http.get("http://192.168.43.221:8888/device-status/chart/" + id)
            .pipe(map(this.extractData));
    }

    controlLight(isLight: boolean) {
        console.log(isLight);
        if (isLight) {
            console.log(isLight);
            return this.http.get("http://192.168.43.221:8888/device/flash-light/control/off").pipe(map(this.extractData));
        } else {
            return this.http.get("http://192.168.43.221:8888/device/flash-light/control/on").pipe(map(this.extractData));
        }
    }

    getAnalytic(time: number){
        return this.http.get("http://192.168.43.221:8888/device-status/analytic/"+time).pipe(map(this.extractData));;
    }

    private extractData(res: Response) {
        let body = res;
        return body || {};
    }
}

