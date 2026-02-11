@echo off
setlocal

REM Create a zip package for sharing/downloading the built EXE.

if not exist dist\SheHulkTransformationGame.exe (
  echo [ERROR] dist\SheHulkTransformationGame.exe not found.
  echo Run build_exe.bat first.
  exit /b 1
)

if not exist release mkdir release

powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'dist\SheHulkTransformationGame.exe' -DestinationPath 'release\SheHulkTransformationGame-win64.zip' -Force"

if errorlevel 1 (
  echo [ERROR] Failed to create release\SheHulkTransformationGame-win64.zip
  exit /b 1
)

echo [OK] Created release\SheHulkTransformationGame-win64.zip
