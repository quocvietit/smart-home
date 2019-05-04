import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
import { NgModule } from '@angular/core';

const config: SocketIoConfig = { url: 'http://localhost', options: {} };

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