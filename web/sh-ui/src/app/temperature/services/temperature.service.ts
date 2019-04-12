import { Injectable } from "@angular/core";
import { Socket } from 'ngx-socket-io';
import { map } from 'rxjs/operators';

@Injectable()
export class TemperatureService {

    constructor(private socket: Socket) { }

    sendMessage(msg: string) {
        this.socket.emit("message", msg);
    }

    getMessage() {
        return this.socket
            .fromEvent("message").subscribe(data => data)
    }
}
