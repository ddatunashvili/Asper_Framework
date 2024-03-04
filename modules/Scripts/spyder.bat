@echo off
call "%~dp0env.bat"
if exist "%APPSDIR%\Scripts\spyder.exe" (
    "%APPSDIR%\Scripts\spyder.exe" %*
) else (
    start "" https://www.portabledevapps.net/support-spyder.php
)