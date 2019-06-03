import { NgModule } from '@angular/core';
import {
    MatAutocompleteModule,
    MatIconModule,
    MatTabsModule,
    MatTableModule,
    MatFormFieldModule,
    MatSelectModule
} from '@angular/material';

@NgModule({
    exports: [
        // Material Modules
        MatAutocompleteModule,
        MatIconModule,
        MatTabsModule,
        MatTableModule,
        MatFormFieldModule,
        MatSelectModule
    ],
    providers: [
    ],
})
export class MaterialModule { }