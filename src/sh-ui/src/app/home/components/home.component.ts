import { Component, OnInit, OnChanges, AfterViewInit, ViewChild } from '@angular/core';
import { StringFormatPipe } from '../../common/pipe/string-format.pipe';
import { TimeChartFormatPipe } from '../../common/pipe/time-chart-format.pipe';
import { InfoHomeComponent } from '../../common/components/info-home/info-home.component';
import { SocketService } from 'src/app/common/services/socket.service';
import { Constants } from 'src/app/common/utilities/constants';
import { TimeService } from 'src/app/common/services/time.service';
import { TimeModel } from 'src/app/common/models/time.model';
import { HomeService } from '../services/home.service';
import { DeviceService } from 'src/app/common/services/device.service';
import { Temperature } from 'src/app/common/models/temperature.model';

@Component({
    selector: 'home-component',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit, OnChanges, AfterViewInit {
    @ViewChild("InfoHomeComponent") infoHome: InfoHomeComponent;

    constants = Constants;

    currentDay: String = this.constants.TIME.DEFAULT.DAY;
    currentMonth: String = this.constants.TIME.DEFAULT.MONTH;
    currentYear: String = this.constants.TIME.DEFAULT.YEAR;
    currentTime: String;
    temperature: String = "--°C";
    humidity: String = "--%";
    light: String = "--";
    gas: String = "--";
    flashLight: String = "--";
    model: Temperature;

    constructor(
        private stringFormat: StringFormatPipe,
        private timeChartFormat: TimeChartFormatPipe,
        private socketService: SocketService,
        private timeService: TimeService,
        private homeService: HomeService,
        private deviceService: DeviceService
    ) {
        this.homeService.getDataFromDatabase();
        this.getDate();
        this.initData();
    }

    ngOnInit() {
        this.initSocket();
    }

    ngOnChanges() {
    }

    ngAfterViewInit() { }

    initData(){
        
        // this.deviceService.getValue(1).toPromise().then((res: any) => {
        // });
        // this.temperature = this.model.day;
        // this.deviceService.getValue(1).toPromise().then((res: any) => {
        //     this.temperature = res.value + "°C";
        // });  this.deviceService.getValue(2).toPromise().then((res: any) => {
        //     this.humidity = res.value + "°C";
        // })
        // this.deviceService.getValue(3).toPromise().then((res: any) => {
        //     this.setLight(res.value.toString());
        // });
        // this.deviceService.getValue(4).toPromise().then((res: any) => {
        //     this.setGas(res.value.toString());
        // });
        // this.deviceService.getValue(5).toPromise().then((res: any) => {
        //     this.setFlashLight(res.value.toString());
        // });

        // this.temperature = this.homeService.temperature + "°C";
        // this.humidity = this.homeService.temperature + "%";
        // this.setLight(this.homeService.temperature.toString());
        // this.setGas(this.homeService.isGas.toString());
        // this.setFlashLight(this.homeService.isFlashLight.toString());
    }

    initSocket() {
        console.log("Open socket....")
        this.socketService.getMessage("temperature").subscribe(
            data => {
                this.temperature = data.toString() + "°C";
            },
            err => {
                console.log("err: " + err);
            }
        );

        this.socketService.getMessage("humidity").subscribe(
            data => {
                this.humidity = data.toString() + "%";
            },
            err => {
                console.log("err: " + err);
            }
        );

        this.socketService.getMessage("light").subscribe(
            data => {
                let value = data.toString();
                this.setLight(value);
            },
            err => {
                console.log("err: " + err);
            }
        );

        this.socketService.getMessage("gas").subscribe(
            data => {
                let value = data.toString();
                this.setGas(value);
            },
            err => {
                console.log("err: " + err);
            }
        );

        this.socketService.getMessage("flashLight").subscribe(
            data => {
                let value = data.toString();
                this.setFlashLight(value);
            },
            err => {
                console.log("err: " + err);
            }
        );
    }

    getDate() {
        this.timeService.getTime().subscribe(
            data => {
                let time = data as TimeModel;
                this.currentDay = time.day;
                this.currentMonth = time.month;
                this.currentYear = time.year;
                this.currentTime = time.time;
            },
            err => {
                console.log("Get time error: " + err);
            }
        );
    }

    setLight(value: String){
        if (value === "0") {
            this.light = "Sáng";
        } else {
            this.light = "Tối";
        }
    }

    setGas(value: String){
        if (value === "0") {
            this.gas = "Không";
        } else {
            this.gas = "Có";
        }
    }

    setFlashLight(value: String){
        if (value === "0") {
            this.flashLight = "Tắt";
        } else {
            this.flashLight = "Bật";
        }
    }

}