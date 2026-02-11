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

REM Include streamlit_app.py so launcher can run it from bundled temp folder.
pyinstaller --noconfirm --clean --onefile --name SheHulkTransformationGame --add-data "streamlit_app.py;." launcher.py

echo.
echo Build complete. EXE path:
echo   dist\SheHulkTransformationGame.exe
