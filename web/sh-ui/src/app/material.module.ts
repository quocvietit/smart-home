import { NgModule } from '@angular/core';
import {
    MatAutocompleteModule,
    MatIconModule,
    MatTabsModule,
    MatTableModule
} from '@angular/material';

@NgModule({
    exports: [
        // Material Modules
        MatAutocompleteModule,
        MatIconModule,
        MatTabsModule,
        MatTableModule
    ],
    providers: [
    ],
})
export class MaterialModule { }