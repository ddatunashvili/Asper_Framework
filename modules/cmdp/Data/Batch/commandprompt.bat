@echo off
cd ..
cd Scripts
call "env.bat"
color 07
prompt $p$g
title Python Portable Console
cls
echo ================ INSTALL / UPGRADE packages ================
echo =                                                          =
echo = install   : python -m pip install package_name           =
echo = upgrade   : python -m pip install --upgrade package_name =
echo = uninstall : python -m pip uninstall package_name         =
echo = list      : python -m pip list                           =
echo =                                                          =
echo ============================================================
echo ====================== PYTHON CONSOLE ======================
echo =                                                          =
echo = open      : python                                       =
echo = close     : quit()                                       =
echo =                                                          =
echo ============================================================
