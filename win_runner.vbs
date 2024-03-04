Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c ""package.bat""", 0, False
Set WshShell = Nothing
