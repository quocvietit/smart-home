import { NgModule } from '@angular/core';
import {
    MatAutocompleteModule,
    MatIconModule,
    MatTabsModule
} from '@angular/material';
import { CdkTableModule } from '@angular/cdk/table';
import { A11yModule } from '@angular/cdk/a11y';
import { BidiModule } from '@angular/cdk/bidi';
import { OverlayModule } from '@angular/cdk/overlay';
import { PlatformModule } from '@angular/cdk/platform';
import { ObserversModule } from '@angular/cdk/observers';
import { PortalModule } from '@angular/cdk/portal';

@NgModule({
    exports: [
        // Material Modules
        MatAutocompleteModule,
        MatIconModule,
        MatTabsModule,
    ],
    providers: [
    ],
})
export class MaterialModule { }