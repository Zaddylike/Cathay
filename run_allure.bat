@echo off

call clean_pycache.bat

echo Generating Allure HTML report...
allure generate reports/allure-results -o reports/allure-report --clean

echo Opening Allure report...
allure open reports/allure-report

pause