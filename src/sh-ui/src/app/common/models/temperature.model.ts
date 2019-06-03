import { Device } from './device.model';

export class Temperature extends Device{
    constructor(params?: any){
        super();
        this.value = params.value;
    }
}