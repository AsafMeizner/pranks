:: this is a code that opens never gonna give you up in youtube and puts volume to max


@if (@a==@b) @end /*

:: batch portion

@ECHO OFF

start " " https://www.youtube.com/watch?v=QtBDL8EiNZo

cscript /e:jscript "%~f0"


:: JScript portion */

var shl = new ActiveXObject("WScript.Shell");
for (var i=0; i<50; i++) {
    shl.SendKeys(String.fromCharCode(0xAF));
}