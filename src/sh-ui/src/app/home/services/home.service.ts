import { Injectable } from "@angular/core";
import { SocketService } from 'src/app/common/services/socket.service';
import { TimeChartFormatPipe } from 'src/app/common/pipe/time-chart-format.pipe';
import { DeviceService } from 'src/app/common/services/device.service';

@Injectable()
export class HomeService {
    temperature: any;
    humidity: any;
    isLight: any;
    isGas: any;
    isFlashLight: any;

    constructor(private socketService: SocketService,
        private deviceService: DeviceService,
        private timeChartService: TimeChartFormatPipe) {
        this.getDataFromDatabase();
    }

    getDataFromDatabase() {
        this.deviceService.getValue(1).toPromise().then(
            res => {
                console.log(res);
            },
            err => {
                console.log("Error get device temperature: " + err);
            }
        );

        this.deviceService.getValue(2).toPromise().then(
            res => {
                this.humidity = res['value'];
            },
            err => {
                console.log("Error get device humidity: " + err);
            }
        );

        this.deviceService.getValue(3).toPromise().then(
            res => {
                this.isLight = res['value'] === "0"?false: true;
            },
            err => {
                console.log("Error get device light: " + err);
            }
        );

        this.deviceService.getValue(4).toPromise().then(
            res => {
                this.isGas = res['value'] === "0"?false: true;
            },
            err => {
                console.log("Error get device light: " + err);
            }
        );

        this.deviceService.getValue(5).toPromise().then(
            res => {
                this.isFlashLight = res['value'] === "0"?false: true;
            },
            err => {
                console.log("Error get device light: " + err);
            }
        );
    }
}