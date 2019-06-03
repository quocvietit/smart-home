import {Component, OnInit, OnChanges, AfterViewInit} from '@angular/core';

@Component({
    selector: 'category-component',
    templateUrl: './category.component.html',
    styleUrls: ['./category.component.css']
})

export class CategoryComponent implements OnInit, OnChanges, AfterViewInit{
    private links = [
        { label: 'Dashboard', path: '/home'},
        { label: 'Monitor', path: '/monitor'},
        { label: 'Analytic', path: '/analytic'},
        { label: 'About', path: '/about'}
    ]
    
    constructor(){};

    ngOnInit() {};

    ngOnChanges(){};

    ngAfterViewInit() {};
}