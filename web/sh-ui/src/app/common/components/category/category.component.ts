import {Component, OnInit, OnChanges, AfterViewInit} from '@angular/core';

@Component({
    selector: 'category-component',
    templateUrl: './category.component.html',
    styleUrls: ['./category.component.css']
})

export class CategoryComponent implements OnInit, OnChanges, AfterViewInit{
    private links = [
        { label: 'Home', path: '/home'},
        { label: 'Temperature', path: '/temperature'},
        { label: 'Humidity', path: '/humidity'},
        { label: 'Monitor', path: '/monitor'},
        { label: 'About', path: '/about'}
    ]
    
    constructor(){};

    ngOnInit() {};

    ngOnChanges(){};

    ngAfterViewInit() {};
}