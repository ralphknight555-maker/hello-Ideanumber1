@echo off
setlocal

REM Smoke-test launcher for the built Windows executable.

if not exist dist\SheHulkTransformationGame.exe (
  echo [ERROR] dist\SheHulkTransformationGame.exe not found.
  echo Run build_exe.bat first.
  exit /b 1
)

echo [OK] Found dist\SheHulkTransformationGame.exe
echo Launching executable...
start "SheHulkTransformationGame" dist\SheHulkTransformationGame.exe

echo.
echo If your browser did not open automatically, visit:
echo   http://localhost:8501
