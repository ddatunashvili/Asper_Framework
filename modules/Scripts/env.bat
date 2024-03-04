@echo off
SET parent=%~dp0
FOR %%a IN ("%parent:~0,-1%") DO SET grandparent=%%~dpa
FOR %%a IN ("%grandparent:~0,-1%") DO SET grandgrandparent=%%~dpa
set ROOTDIR=%grandgrandparent%
set APPSDIR=%ROOTDIR%apps
set APPDATA=%ROOTDIR%apps
set HOME=%ROOTDIR%workspace
set JUPYTER_DATA_DIR=%HOME%
set PATH=%ROOTDIR%;%APPSDIR%;%APPSDIR%\DLLs;%APPSDIR%\Lib;%APPSDIR%\Scripts;%APPSDIR%\Lib\site-packages\PyQt5;