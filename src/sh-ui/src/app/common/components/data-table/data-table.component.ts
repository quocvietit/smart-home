import {Component, OnInit, OnChanges, AfterViewInit, Input, ViewChild} from '@angular/core';
import { MatPaginator } from '@angular/material';

@Component({
    selector: 'data-table-component',
    templateUrl: './data-table.component.html',
    styleUrls: ['./data-table.component.css']
})

export class DataTableComponent implements OnInit, OnChanges, AfterViewInit{
    @Input() cols: any;
    @Input() data: any;

    @ViewChild(MatPaginator) paginator: MatPaginator;
    
    constructor(){};

    ngOnInit() {};

    ngOnChanges(){};

    ngAfterViewInit() {};
}