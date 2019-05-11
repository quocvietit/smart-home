import { OnInit, OnChanges, AfterViewInit, Component, ViewChild } from '@angular/core';
import { DeviceService } from '../../services/device.service';
import { MatSelect } from '@angular/material';

@Component({
    selector: 'analytic-component',
    templateUrl: './analytic.component.html',
    styleUrls: ['./analytic.component.css']
})

export class AnalyticComponent implements OnInit, OnChanges, AfterViewInit {
    isLoad: boolean = false;
    isError: boolean = false;
    selected: number;
    temperature:any = {
        mode: "",
        mean: "",
        min: "",
        max: "",
    }
    humidity: any = {
        mode: "",
        mean: "",
        min: "",
        max: "",
    }
    constructor(
        private deviceService: DeviceService
    ){

    }

    ngOnInit(){

    }

    ngOnChanges(){

    }

    ngAfterViewInit(){

    }

   getData(){
        this.deviceService.getAnalytic(this.selected).subscribe(
            data =>{
                console.log(this.selected);
                console.log(data);
                this.temperature.mean = data['temperature']['mean'];
                this.temperature.min = data['temperature']['min'];
                this.temperature.max = data['temperature']['max'];
                this.temperature.mode = data['temperature']['mode'];
                this.humidity.mean = data['humidity']['mean'];
                this.humidity.min = data['humidity']['min'];
                this.humidity.max = data['humidity']['max'];
                this.humidity.mode = data['humidity']['mode'];
                this.isLoad = true;
            }, 
            err => {
                this.isError = true;
                console.log("Error: "+err);
            }
        );
   }

}