import { Pipe, PipeTransform } from "@angular/core";

@Pipe({ name: "stringFormat" })
export class StringFormatPipe implements PipeTransform {
    transform(value: string, args?: any[]): string {
        if (!value) { return ""; }

        for (let key in args) {
            value = value.replace("{" + key + "}", args[key]);
        }
        return value;
    }
}