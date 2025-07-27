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
python main.py %yt_url%

ENDLOCAL
pause
