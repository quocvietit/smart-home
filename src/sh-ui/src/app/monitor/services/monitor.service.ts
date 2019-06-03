import { Injectable } from "@angular/core";
import { SocketService } from 'src/app/common/services/socket.service';
import { TimeChartFormatPipe } from 'src/app/common/pipe/time-chart-format.pipe';
import { DeviceService } from 'src/app/common/services/device.service';

@Injectable()
export class MonitorService {
    temperatureData: any = [NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN] ;
    temperatureLabel: any = ["", "", "", "", "", "", "", "", "", ""];
    humidityData:any = [NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN];
    humidityLabel:any = ["", "", "", "", "", "", "", "", "", ""];
    isLight: boolean = false;
    isGas: boolean = false;

    constructor(private socketService: SocketService,
        private deviceService: DeviceService,
        private timeChartService: TimeChartFormatPipe) { 
        this.getDataFromDatabase();
    }

    getDataFromDatabase(){
        this.deviceService.getValueForChart(1).toPromise().then(
            res =>{
                this.handleTemperatureData(res);
            },
            err => {
                console.log("Error get device temperature: " + err);
            }
        );

        this.deviceService.getValueForChart(2).toPromise().then(
            res =>{
                this.handleHumidityData(res);
            },
            err => {
                console.log("Error get device humidity: " + err);
            }
        );

        this.deviceService.getValue(5).toPromise().then(
            res =>{
                this.handleLightData(res);
            },
            err => {
                console.log("Error get device light: " + err);
            }
        );

        this.deviceService.getValue(4).toPromise().then(
            res =>{
                this.handleGasData(res);
            },
            err => {
                console.log("Error get device gas: " + err);
            }
        );
    }

    handleTemperatureData(res){
        let data = JSON.parse(JSON.stringify(res)) as Array<any>;
        data.forEach(element => {
            let time = new Date(element['time']);
            let label = this.timeChartService.transFormDateWithOutTimeZoneToHoursAndMinutesAndSecond(time);
            this.temperatureData.push(element['value']);
            this.temperatureData.shift();
            this.temperatureLabel.push(label);
            this.temperatureLabel.shift();
        });
    }

    handleHumidityData(res){
        let data = JSON.parse(JSON.stringify(res)) as Array<any>;
        data.forEach(element => {
            let time = new Date(element['time']);
            let label = this.timeChartService.transFormDateWithOutTimeZoneToHoursAndMinutesAndSecond(time);
            this.humidityData.push(element['value']);
            this.humidityData.shift();
            this.humidityLabel.push(label);
            this.humidityLabel.shift();
        });
    }

    handleLightData(res){
        let data = JSON.parse(JSON.stringify(res));
        this.isLight = data['value'] === '0'? false: true;
    }

    handleGasData(res){
        let data = JSON.parse(JSON.stringify(res));
        this.isGas = data['value'] === '0'? false: true;
    }

    getLightStatus(){
        return this.isLight;
    }
}