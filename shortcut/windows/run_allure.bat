@echo off
setlocal

pushd "%~dp0\..\.."
call "%~dp0clean_pycache.bat"

if not exist "node_modules\.bin\allure.cmd" (
    echo Allure CLI not found. Run "npm ci" first.
    popd
    exit /b 1
)

echo Generating Allure HTML report...
call "node_modules\.bin\allure.cmd" generate reports/allure-results -o reports/allure-report --clean
if errorlevel 1 (
    popd
    exit /b 1
)

echo Opening Allure report...
call "node_modules\.bin\allure.cmd" open reports/allure-report

popd
