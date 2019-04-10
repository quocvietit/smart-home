import {Component, OnInit, OnChanges, AfterViewInit} from '@angular/core';

@Component({
    selector: 'category-component',
    templateUrl: './category.component.html',
    styleUrls: ['./category.component.css']
})

export class CategoryComponent implements OnInit, OnChanges, AfterViewInit{
    private links = [
        { label: 'Smart Home', path: '/home'},
        { label: 'Temperature', path: '/temperature'},
        { label: 'Humidity', path: '/page-not-found'},
        { label: 'Monitor', path: '/page-not-found'}
    ]
    
    constructor(){};

    ngOnInit() {};

    ngOnChanges(){};

    ngAfterViewInit() {};
}