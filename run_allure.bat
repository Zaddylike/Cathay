@echo off

echo Generating Allure HTML report...
allure generate reports/allure-results -o reports/allure-report --clean

echo Opening Allure report...
allure open reports/allure-report

pause