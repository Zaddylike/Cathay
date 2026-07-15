@echo off
setlocal

pushd "%~dp0\..\.."

if not exist "node_modules\.bin\allure.cmd" (
    echo Allure CLI not found. Run "npm ci" first.
    popd
    exit /b 1
)

call "node_modules\.bin\allure.cmd" open reports/allure-report
popd
