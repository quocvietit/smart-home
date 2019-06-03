import { Injectable } from "@angular/core";
import { Socket } from 'ngx-socket-io';
import { map } from 'rxjs/operators';

@Injectable()
export class SocketService {

    constructor(private socket: Socket) { 
    }

    sendMessage(topic: string, msg: string) {
        this.socket.emit(topic, msg);
    }

    getMessage(topic: string) {
        return this.socket
            .fromEvent(topic).pipe(map(data => data));
    }
}