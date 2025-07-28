@echo off
SETLOCAL

echo Checking virtual environment...

IF NOT EXIST "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing requirements (if needed)...
pip install -r requirements.txt >nul 2>&1

echo.
set /p yt_url="Enter YouTube URL: "
echo Choose summary mode:
echo [1] Brief
echo [2] Detailed (default)
set /p summary_mode="Enter choice (1 or 2): "

if "%summary_mode%"=="1" (
    set mode=--brief
) else (
    set mode=--detailed
)

python main.py "%yt_url%" %mode%

ENDLOCAL
pause
