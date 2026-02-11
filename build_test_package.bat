@echo off
setlocal

REM One-command Windows flow: build EXE, smoke-test launch, and create ZIP package.

call build_exe.bat
if errorlevel 1 (
  echo [ERROR] build_exe.bat failed.
  exit /b 1
)

call test_exe.bat
if errorlevel 1 (
  echo [ERROR] test_exe.bat failed.
  exit /b 1
)

call package_download.bat
if errorlevel 1 (
  echo [ERROR] package_download.bat failed.
  exit /b 1
)

echo.
echo [OK] All steps completed.
echo Downloadable ZIP:
echo   release\SheHulkTransformationGame-win64.zip
