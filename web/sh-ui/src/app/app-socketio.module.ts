import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
import { NgModule } from '@angular/core';

const config: SocketIoConfig = { url: 'http://192.168.43.221', options: {} };

@NgModule({
    declarations: [],
    imports: [
        SocketIoModule.forRoot(config)
    ],
    exports: [
        SocketIoModule
    ]
  })
  export class AppSocketIOModule { }