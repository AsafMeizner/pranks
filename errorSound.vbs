Set objShell = CreateObject("WScript.Shell")
soundFile = "C:\Windows\Media\Windows Foreground.wav"

Do While True
    ' Generate a random number between 30 and 60
    waitTime = Int((60 - 30 + 1) * Rnd + 30)
    
    ' Play the sound
    objShell.Run "wmplayer " & Chr(34) & soundFile & Chr(34), 0, True
    
    ' Wait for the random amount of seconds
    WScript.Sleep waitTime * 1000
Loop
