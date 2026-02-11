@echo off
setlocal

REM Build a Windows executable for the She-Hulk Streamlit app.
REM Run this file from a Windows command prompt.

if not exist venv (
  py -m venv venv
)

call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt pyinstaller

pyinstaller --noconfirm --clean --onefile --name SheHulkTransformationGame launcher.py

echo.
echo Build complete. EXE path:
echo   dist\SheHulkTransformationGame.exe
