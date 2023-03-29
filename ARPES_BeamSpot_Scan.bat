@echo off
rem D:
rem cd D:\RIXS09_Position_Motion
@echo off
 
set CurrentPath=%~dp0
set P1Path=
set P2Path=
set P3Path=
set P4Path=
set P5Path=
 
:begin
for /f "tokens=1,* delims=\" %%i in ("%CurrentPath%") do (set content=%%i&&set CurrentPath=%%j)
if "%P1Path%%content%\" == "%~dp0" goto end
set P5Path=%P4Path%
set P4Path=%P3Path%
set P3Path=%P2Path%
set P2Path=%P1Path%
set P1Path=%P1Path%%content%\
goto begin
:end
echo BatPath=%~dp0
rem echo P1Path=%P1Path%
rem echo P2Path=%P2Path%
rem echo P3Path=%P3Path%
rem echo P4Path=%P4Path%
rem echo P5Path=%P5Path%

set pwd=%cd%
rem echo %pwd%
set mainPY=main.py
set mainAPP=%pwd%\%mainPY%
echo %mainAPP%
rem set pythonpath=C:/Python310/python.exe
set pythonpath=%P1Path%\PythonENV\ARPES09\Scripts\python.exe
echo pythonpath=%pwd%
rem cd /d %~dp0
rem start python main.py
start %pythonpath% %mainAPP%
pause
rem exit
