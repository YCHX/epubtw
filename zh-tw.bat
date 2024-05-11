@echo off
setlocal

set PYTHON_EXE="python"

if "%~1"=="" (
    echo No file specified.
    pause
    exit /b
)

:next
if "%~1"=="" goto done
echo Processing: %~1
"%PYTHON_EXE%" "src\\main.py" "%~1"
shift
goto next

:done