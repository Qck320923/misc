@echo off
title EasyShutdown v0.0.1
echo EasyShutdown v0.0.1 is running!

echo Waiting for the operation...

python main.py

:wait_for_file
if not exist choice.txt (
    timeout /t 1 >nul
    goto wait_for_file
)

echo Get a response.

set /p CHOICE=<choice.txt
set time=5

if "%CHOICE%"=="shutdown" (
    shutdown /s /t %time%
) else if "%CHOICE%"=="sleep" (
    rundll32.exe user32.dll LockWorkStation
) else if "%CHOICE%"=="reboot" (
    shutdown /r /t %time%
) else if "%CHOICE%"=="close" (
    echo There is no operation, and the program has ended.
) else (
    echo Error: Invalid selection or file is corrupted.
)

del choice.txt
rd /s /q __pycache__