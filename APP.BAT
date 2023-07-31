@echo off

REM Check if Python is installed
where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed on this system.
    exit /b
)

REM Get the Python executable path
for /f "delims=" %%I in ('where python') do set "python_path=%%I"

REM Check if a Python file is provided as an argument
if "%~1"=="" (
    echo Please provide the path to a Python file as an argument.
    exit /b
)

REM Run the Python file using the Python executable path
"%python_path%" "%~1"
