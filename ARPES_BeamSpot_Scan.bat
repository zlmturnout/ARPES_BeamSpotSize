@echo off
rem D:
rem cd D:\RIXS09_Position_Motion
set pwd=%cd%
echo %pwd%
set mainPY=main.py
set mainAPP=%pwd%\%mainPY%
echo %mainAPP%
set pythonpath=C:/Python310/python.exe
cd /d %~dp0
rem start python main.py
start %pythonpath% %mainAPP%
pause
rem exit
