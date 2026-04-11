@echo off
cd /d "%~dp0"
echo Starting Traffic Sign Detection App...
venv\Scripts\python webcam_app.py
pause
