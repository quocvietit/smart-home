import { Injectable } from '@angular/core';

@Injectable()
export class AnalyticsService {
    constructor(){
    }

    calAverage(array: any): string{
        let sum = 0;
        console.log(array);
        array.forEach(e => {
            sum+=e
            
        });
        
        let average = sum/array.length;
        console.log("AVE: "+ average +" "+ array.length);
        return average.toFixed(0);
    }
}