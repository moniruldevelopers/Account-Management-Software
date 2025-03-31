@echo off
REM Change to your project directory
cd /d "G:\jisc accounting software"

REM Activate the virtual environment
call "G:\jisc accounting software\venv\Scripts\activate.bat"

REM Start the Django development server
python manage.py runserver 192.168.0.110:8000

pause
