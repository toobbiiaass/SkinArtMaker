@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install it: https://www.python.org/downloads/
    pause
    exit /b
)

REM Check if Pillow is installed
python -c "from PIL import Image" >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Pillow is not installed. Installing now...
    pip install pillow
)

REM Check if tkinter is installed
python -c "from tkinter import Tk" >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo tkinter is not installed. tkinter is usually bundled with Python. Please make sure you have it installed.
    pause
    exit /b
)

REM Check if colorama is installed
python -c "from colorama import init, Fore" >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Colorama is not installed. Installing now...
    pip install colorama
)

REM Run the Python script
python SkinArtMaker.py
pause
