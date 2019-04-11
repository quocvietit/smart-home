import {Component, OnInit, OnChanges, AfterViewInit, Input} from '@angular/core';
import { Constants } from '../../utilities/constants';

@Component({
    selector: 'title-component',
    templateUrl: './title.component.html',
    styleUrls: ['./title.component.css']
})

export class TitleComponent implements OnInit, OnChanges, AfterViewInit{

    constants = Constants;

    constructor(){};

    ngOnInit() {
    };

    ngOnChanges(){};

    ngAfterViewInit() {};
}