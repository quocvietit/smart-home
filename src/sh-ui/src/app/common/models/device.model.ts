export class Device{
    id: number
    deviceId: number;
    value: string;
    time: string;

    constructor(params?: any){
        this.id = params.id;
        this.deviceId = params.device_id;
        this.time = params.time;
        this.value = params.value;
    }
}