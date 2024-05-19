@echo off
setlocal

set PYTHON_EXE="python"

if "%~1"=="" (
    echo No file specified.
    pause
    exit /b
)

echo Debugging Version Activated
echo Initial PYTHON_EXE=%PYTHON_EXE%

:next
if "%~1"=="" (
    echo No more files to process.
    goto done
)
echo Processing: %~1
echo Run Command: "%PYTHON_EXE%" "src\\main.py" "%~1"
"%PYTHON_EXE%" "src\\main.py" "%~1"
if %ERRORLEVEL% NEQ 0 (
    echo Error encountered during processing: %ERRORLEVEL%
) else (
    echo Processing completed successfully for: %~1
)
shift
echo Next file argument: %~1
goto next

:done
echo All files processed.
