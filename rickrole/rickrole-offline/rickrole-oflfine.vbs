'this is a code that opens never gonna give you up in vbs and puts volume to max

Set WshShell = CreateObject("WScript.Shell")

WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))

Dim oPlayer
Set oPlayer = CreateObject("WMPlayer.OCX")


' Play audio
Set WshShell = CreateObject("WScript.Shell")
strCurDir = WshShell.CurrentDirectory

oPlayer.URL = strCurDir & "\rickrole.mp3"
oPlayer.controls.play 
While oPlayer.playState <> 1 ' 1 = Stopped
  WScript.Sleep 100
  WshShell.SendKeys(chr(&hAF))
  open "C:\WINDOWS\system32\cmd.exe"
Wend

' Release the audio file
oPlayer.close